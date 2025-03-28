import sqlite3

def create_db():
    con = sqlite3.connect(database="bms.db")  # Changed database name to "bms.db"
    cur = con.cursor()

    # Create table for chawl customers
    cur.execute("""
        CREATE TABLE IF NOT EXISTS customer(
            customer_id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT,
            gender TEXT,
            date_of_purchase TEXT,  -- Changed from dob to date_of_purchase
            contact TEXT,
            chawl_no TEXT,
            room_no TEXT,
            room_price TEXT,
            room_area TEXT,  -- Added room_area column
            state TEXT,
            address TEXT
        )
    """)

    # Create table for payments
    cur.execute("""
        CREATE TABLE IF NOT EXISTS payments (
            payment_id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_id TEXT NOT NULL,  -- Changed to TEXT to match Python code
            name TEXT NOT NULL,
            payment_date TEXT NOT NULL,  -- Full date of payment
            amount REAL NOT NULL,
            payment_type TEXT NOT NULL,
            cheque_number TEXT,
            bank_name TEXT,
            FOREIGN KEY (customer_id) REFERENCES customer(customer_id)
        )
    """)

    # Add missing columns to the customer table if they don't exist
    cur.execute("PRAGMA table_info(customer)")
    columns = [column[1] for column in cur.fetchall()]
    if "room_area" not in columns:
        cur.execute("ALTER TABLE customer ADD COLUMN room_area TEXT")

    # Add missing columns to the payments table if they don't exist
    cur.execute("PRAGMA table_info(payments)")
    columns = [column[1] for column in cur.fetchall()]
    required_columns = ["customer_id", "name", "payment_date", "amount", "payment_type", "cheque_number", "bank_name"]
    for column in required_columns:
        if column not in columns:
            cur.execute(f"ALTER TABLE payments ADD COLUMN {column} TEXT")

    # Drop the month column if it exists (since it's no longer needed)
    if "month" in columns:
        cur.execute("ALTER TABLE payments DROP COLUMN month")

    con.commit()
    con.close()

# Call the function to create the database and tables
create_db()