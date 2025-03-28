from tkinter import *
from tkinter import messagebox
import tkinter
from PIL import Image, ImageTk
from tkinter import ttk
import sqlite3
import re
from datetime import datetime
from tkcalendar import DateEntry
from loginn import Loginn


class CustomerClass:
    def __init__(self, root, dashboard):
        self.root = root
        self.dashboard = dashboard  # Store the dashboard instance
        self.root.title("श्री समर्थ कृपा एंटरप्रायझेस")
        self.root.geometry("1366x770")
        self.root.resizable(False, False)

        # bg image
        self.bg_img = Image.open("images/blurbg.png")
        self.bg_img = self.bg_img.resize((1500, 900))
        self.bg_img = ImageTk.PhotoImage(self.bg_img)
        self.lab_bg = Label(self.root, image=self.bg_img).place(x=1, y=1, width=1500, height=900)

        # title
        title = Label(self.root, text="श्री समर्थ कृपा एंटरप्रायझेस", font=("Time new romes", 20, "bold"), bg="#CD0000", fg="white").place(x=10, y=15, width=1500, height=50)

        # variables
        self.var_customer_id = StringVar()
        self.var_name = StringVar()
        self.var_email = StringVar()
        self.var_gender = StringVar()
        self.var_date_of_purchase = StringVar()
        self.var_contact = StringVar()
        self.var_chawl_no = StringVar()
        self.var_room_no = StringVar()
        self.var_room_price = StringVar()
        self.var_room_area = StringVar()
        self.var_state = StringVar()
        self.var_city = StringVar()
        self.var_pin = StringVar()

        # Widgets
        lbl_customer_id = Label(self.root, text="Customer ID", font=("Goudy old style", 20, "bold"), bg="white", fg="black").place(x=18, y=100)
        lbl_Name = Label(self.root, text="Name", font=("Goudy old style", 20, "bold"), bg="white", fg="black").place(x=18, y=170)
        lbl_Email = Label(self.root, text="Email", font=("Goudy old style", 20, "bold"), bg="white", fg="black").place(x=18, y=240)
        lbl_Gender = Label(self.root, text="Gender", font=("Goudy old style", 20, "bold"), bg="white", fg="black").place(x=18, y=310)
        lbl_State = Label(self.root, text="State", font=("Goudy old style", 20, "bold"), bg="white", fg="black").place(x=18, y=380)
        lbl_room_price = Label(self.root, text="Room Price", font=("Goudy old style", 20, "bold"), bg="white", fg="black").place(x=18, y=450)
        lbl_room_area = Label(self.root, text="Room Area", font=("Goudy old style", 20, "bold"), bg="white", fg="black").place(x=18, y=520)
        lbl_Address = Label(self.root, text="Address", font=("Goudy old style", 20, "bold"), bg="white", fg="black").place(x=18, y=590)

        # entry fields 1st col
        self.txt_customer_id = Entry(self.root, textvariable=self.var_customer_id, font=("Goudy old style", 20, "bold"), bg="light yellow", fg="black")
        self.txt_customer_id.place(x=180, y=100, width=230)
        text_name = Entry(self.root, textvariable=self.var_name, font=("Goudy old style", 20, "bold"), bg="light yellow", fg="black").place(x=180, y=170, width=230)
        text_email = Entry(self.root, textvariable=self.var_email, font=("Goudy old style", 20, "bold"), bg="light yellow", fg="black").place(x=180, y=240, width=230)
        self.text_gender = ttk.Combobox(self.root, textvariable=self.var_gender, values=("Select", "Male", "Female", "Other"), font=("Goudy old style", 20, "bold"), state='readonly', justify=CENTER)
        self.text_gender.place(x=180, y=310, width=230)
        self.text_gender.current(0)
        text_state = Entry(self.root, textvariable=self.var_state, font=("Goudy old style", 20, "bold"), bg="light yellow", fg="black").place(x=180, y=380, width=230)
        text_room_price = Entry(self.root, textvariable=self.var_room_price, font=("Goudy old style", 20, "bold"), bg="light yellow", fg="black").place(x=180, y=446, width=300, height=40)
        text_room_area = Entry(self.root, textvariable=self.var_room_area, font=("Goudy old style", 20, "bold"), bg="light yellow", fg="black").place(x=180, y=520, width=300, height=40)

        # Column 2
        lbl_date_of_purchase = Label(self.root, text="Date of Purchase", font=("Goudy old style", 20, "bold"), bg="white", fg="black").place(x=430, y=100)
        lbl_contact = Label(self.root, text="Contact", font=("Goudy old style", 20, "bold"), bg="white", fg="black").place(x=430, y=170)
        lbl_chawl_no = Label(self.root, text="Chawl No.", font=("Goudy old style", 20, "bold"), bg="white", fg="black").place(x=430, y=240)
        lbl_room_no = Label(self.root, text="Room No.", font=("Goudy old style", 20, "bold"), bg="white", fg="black").place(x=430, y=310)

        # entry fields 2
        self.text_date_of_purchase = DateEntry(self.root, textvariable=self.var_date_of_purchase, font=("Goudy old style", 20), bg="light yellow", fg="black", date_pattern="yyyy-mm-dd", state="readonly")
        self.text_date_of_purchase.place(x=640, y=100, width=150)

        text_contact = Entry(self.root, textvariable=self.var_contact, font=("Goudy old style", 20, "bold"), bg="light yellow", fg="black").place(x=540, y=170, width=250)
        text_chawl_no = Entry(self.root, textvariable=self.var_chawl_no, font=("Goudy old style", 20, "bold"), bg="light yellow", fg="black").place(x=560, y=240, width=200)
        text_room_no = Entry(self.root, textvariable=self.var_room_no, font=("Goudy old style", 20, "bold"), bg="light yellow", fg="black").place(x=560, y=310, width=200)

        # txt address
        self.text_address = Text(self.root, font=("Goudy old style", 20, "bold"), bg="light yellow", fg="black")
        self.text_address.place(x=180, y=590, width=600, height=120)

        # buttons
        self.btn_add = Button(self.root, text="Save", font=("goudy old style", 15, "bold"), bg="#2196f3", fg="black", cursor="hand2", command=self.add)
        self.btn_add.place(x=50, y=720, width=130, height=45)
        self.btn_update = Button(self.root, text="Update", font=("goudy old style", 15, "bold"), bg="#4caf50", fg="black", cursor="hand2", command=self.update)
        self.btn_update.place(x=200, y=720, width=130, height=45)
        self.btn_delete = Button(self.root, text="Delete", font=("goudy old style", 15, "bold"), bg="#F44336", fg="black", cursor="hand2", command=self.delete)
        self.btn_delete.place(x=350, y=720, width=130, height=45)
        self.btn_clear = Button(self.root, text="Clear", font=("goudy old style", 15, "bold"), bg="#607d8b", fg="black", cursor="hand2", command=self.clear)
        self.btn_clear.place(x=500, y=720, width=130, height=45)
        exit_btn = Button(self.root, text="Exit", font=("Times new romen", 14), fg="black", bg="red", cursor="hand2", command=self.iExit).place(x=1200, y=740, width=100, height=38)
        back_btn = Button(self.root, text="Back to Dashboard", font=("Times new roman", 14), fg="black", bg="lightgray", cursor="hand2", command=self.go_back_to_login).place(x=1000, y=740, width=150, height=38)

        # search panel
        self.var_search = StringVar()
        lbl_search_customer_id = Label(self.root, text="Customer ID", font=("Goudy old style", 20, "bold"), bg="white", fg="black").place(x=800, y=100)
        txt_search_customer_id = Entry(self.root, textvariable=self.var_search, font=("Goudy old style", 20, "bold"), bg="light yellow", fg="black").place(x=980, y=100, width=200, height=38)
        btn_search = Button(self.root, text="Search", font=("goudy old style", 15, "bold"), bg="#03a9f4", fg="black", cursor="hand2", command=self.search).place(x=1190, y=100, width=130, height=38)

        # Content
        self.C_Frame = Frame(self.root, bd=2, relief=RIDGE)
        self.C_Frame.place(x=800, y=200, width=500, height=480)

        # scroll bar placement in the treeview
        scrolly = Scrollbar(self.C_Frame, orient=VERTICAL)
        scrollx = Scrollbar(self.C_Frame, orient=HORIZONTAL)
        self.CustomerTable = ttk.Treeview(self.C_Frame, columns=("customer_id", "name", "email", "gender", "date_of_purchase", "contact", "chawl_no", "room_no", "room_price", "room_area", "state", "address"), xscrollcommand=scrollx.set, yscrollcommand=scrolly.set)
        self.CustomerTable.configure(xscrollcommand=scrollx.set)
        self.CustomerTable.configure(yscrollcommand=scrolly.set)
        scrollx.configure(command=self.CustomerTable.xview)
        scrolly.configure(command=self.CustomerTable.yview)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)

        # Treeview headings
        self.CustomerTable.heading("customer_id", text="Customer ID")
        self.CustomerTable.heading("name", text="Name")
        self.CustomerTable.heading("email", text="Email")
        self.CustomerTable.heading("gender", text="Gender")
        self.CustomerTable.heading("date_of_purchase", text="Date of Purchase")
        self.CustomerTable.heading("contact", text="Contact")
        self.CustomerTable.heading("chawl_no", text="Chawl No.")
        self.CustomerTable.heading("room_no", text="Room No.")
        self.CustomerTable.heading("room_price", text="Room Price")
        self.CustomerTable.heading("room_area", text="Room Area")
        self.CustomerTable.heading("state", text="State")
        self.CustomerTable.heading("address", text="Address")

        # Disable column resizing and make Treeview unchangeable
        for col in self.CustomerTable["columns"]:
            self.CustomerTable.column(col, stretch=False, width=100)
        self.CustomerTable["selectmode"] = "none"

        # Automatically adjust column widths
        self.adjust_column_widths()

        self.CustomerTable.pack(fill=BOTH, expand=1)
        self.CustomerTable.bind("<ButtonRelease-1>", self.get_data)
        self.show()

    def adjust_column_widths(self):
        for col in self.CustomerTable["columns"]:
            self.CustomerTable.column(col, width=100)
            self.CustomerTable.heading(col, text=self.CustomerTable.heading(col)["text"], anchor=CENTER)

    def iExit(self):
        iExit = tkinter.messagebox.askyesno("BMS", "Do you want to exit?", parent=self.root)
        if iExit > 0:
            self.root.destroy()
            return

    def clear(self):
        self.show()
        self.var_customer_id.set("")
        self.var_name.set("")
        self.var_email.set("")
        self.var_gender.set("Select")
        self.var_date_of_purchase.set("")
        self.var_contact.set("")
        self.var_chawl_no.set("")
        self.var_room_no.set("")
        self.var_room_price.set("")
        self.var_room_area.set("")
        self.var_state.set("")
        self.text_address.delete("1.0", END)
        self.txt_customer_id.config(state=NORMAL)
        self.var_search.set("")

    def delete(self):
        con = sqlite3.connect(database="bms.db")
        cur = con.cursor()
        try:
            if self.var_customer_id.get() == "":
                messagebox.showerror("Error", "Customer ID Should be required", parent=self.root)
            else:
                cur.execute("select * from customer where customer_id=?", (self.var_customer_id.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Please select the customer from the list first", parent=self.root)
                else:
                    op = messagebox.askyesno("Confirm", "Do you really want to Delete", parent=self.root)
                    if op == True:
                        cur.execute("delete from customer where customer_id=?", (self.var_customer_id.get(),))
                        con.commit()
                        messagebox.showinfo("Delete", "Customer deleted Successfully", parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"error due to {str(ex)}")

    def get_data(self, ev):
        self.txt_customer_id.config(state='readonly')
        r = self.CustomerTable.focus()
        content = self.CustomerTable.item(r)
        row = content["values"]
        
        if row and len(row) >= 11:
            self.var_customer_id.set(row[0])
            self.var_name.set(row[1])
            self.var_email.set(row[2])
            self.var_gender.set(row[3])
            self.var_date_of_purchase.set(row[4])
            self.var_contact.set(row[5])
            self.var_chawl_no.set(row[6])
            self.var_room_no.set(row[7])
            self.var_room_price.set(row[8])
            self.var_room_area.set(row[9])
            self.var_state.set(row[10])
            self.text_address.delete("1.0", END)
            self.text_address.insert(END, row[11])
        else:
            messagebox.showwarning("Warning", "Selected row is empty or incomplete.", parent=self.root)

    def validate_customer_id(self, customer_id):
        pattern = r"^\d+$"  # Ensure Customer ID is numeric
        if re.match(pattern, customer_id):
            return True
        else:
            return False

    def validate_name(self, name):
        pattern = r"^[a-zA-Z\-'. ]+$"  # Ensure Name contains only letters, spaces, and allowed characters
        if re.match(pattern, name):
            return True
        else:
            return False

    def validate_email(self, email):
        pattern = r"^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$"  # Ensure Email is valid
        if re.match(pattern, email):
            return True
        else:
            return False

    def validate_date_of_purchase(self, date_of_purchase):
        try:
            datetime.strptime(date_of_purchase, '%Y-%m-%d')  # Ensure Date is in YYYY-MM-DD format
            return True
        except Exception as ex:
            return False

    def validate_contact(self, contact):
        pattern = r"^\d{10}$"  # Ensure Contact is exactly 10 digits
        if re.match(pattern, contact):
            return True
        else:
            return False

    def validate_room_price(self, room_price):
        try:
            float(room_price)  # Ensure Room Price is a valid number
            return True
        except ValueError:
            return False

    def validate_room_area(self, room_area):
        try:
            float(room_area)  # Ensure Room Area is a valid number
            return True
        except ValueError:
            return False

    def validate_form(self):
        if not self.validate_customer_id(self.var_customer_id.get()):
            messagebox.showerror("Error", "Invalid Customer ID. It must be numeric.", parent=self.root)
            return False
        if not self.validate_name(self.var_name.get()):
            messagebox.showerror("Error", "Invalid Name. It must contain only letters and spaces.", parent=self.root)
            return False
        if not self.validate_email(self.var_email.get()):
            messagebox.showerror("Error", "Invalid Email. Please enter a valid email address.", parent=self.root)
            return False
        if not self.validate_date_of_purchase(self.var_date_of_purchase.get()):
            messagebox.showerror("Error", "Invalid Date of Purchase. Please enter a valid date (YYYY-MM-DD).", parent=self.root)
            return False
        if not self.validate_contact(self.var_contact.get()):
            messagebox.showerror("Error", "Invalid Contact. It must be exactly 10 digits.", parent=self.root)
            return False
        if not self.validate_room_price(self.var_room_price.get()):
            messagebox.showerror("Error", "Invalid Room Price. It must be a valid number.", parent=self.root)
            return False
        if not self.validate_room_area(self.var_room_area.get()):
            messagebox.showerror("Error", "Invalid Room Area. It must be a valid number.", parent=self.root)
            return False
        if self.var_gender.get() == "Select":
            messagebox.showerror("Error", "Please select a gender.", parent=self.root)
            return False
        if not self.text_address.get("1.0", END).strip():
            messagebox.showerror("Error", "Address cannot be empty.", parent=self.root)
            return False
        return True

    def add(self):
        if not self.validate_form():
            return

        con = sqlite3.connect(database="bms.db")
        cur = con.cursor()
        try:
            cur.execute("select * from customer where customer_id=?", (self.var_customer_id.get(),))
            row = cur.fetchone()
            if row is not None:
                messagebox.showerror("Error", "Customer ID Already Exists", parent=self.root)
            else:
                cur.execute("insert into customer (customer_id, name, email, gender, date_of_purchase, contact, chawl_no, room_no, room_price, room_area, state, address) values(?,?,?,?,?,?,?,?,?,?,?,?)", (
                    self.var_customer_id.get(),
                    self.var_name.get(),
                    self.var_email.get(),
                    self.var_gender.get(),
                    self.var_date_of_purchase.get(),
                    self.var_contact.get(),
                    self.var_chawl_no.get(),
                    self.var_room_no.get(),
                    self.var_room_price.get(),
                    self.var_room_area.get(),
                    self.var_state.get(),
                    self.text_address.get("1.0", END)
                ))
                con.commit()
                messagebox.showinfo("Success", "Customer Successfully Added", parent=self.root)
                self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    def update(self):
        if not self.validate_form():
            return

        con = sqlite3.connect(database="bms.db")
        cur = con.cursor()
        try:
            if self.var_customer_id.get() == "":
                messagebox.showerror("Error", "Customer ID Should be required", parent=self.root)
            else:
                cur.execute("select * from customer where customer_id=?", (self.var_customer_id.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Select Customer from list", parent=self.root)
                else:
                    cur.execute("update customer set name=?, email=?, gender=?, date_of_purchase=?, contact=?, chawl_no=?, room_no=?, room_price=?, room_area=?, state=?, address=? where customer_id=?", (
                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_date_of_purchase.get(),
                        self.var_contact.get(),
                        self.var_chawl_no.get(),
                        self.var_room_no.get(),
                        self.var_room_price.get(),
                        self.var_room_area.get(),
                        self.var_state.get(),
                        self.text_address.get("1.0", END),
                        self.var_customer_id.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Customer Update Successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"error due to {str(ex)}")

    def show(self):
        con = sqlite3.connect(database="bms.db")
        cur = con.cursor()
        try:
            cur.execute("select * from customer")
            rows = cur.fetchall()
            self.CustomerTable.delete(*self.CustomerTable.get_children())
            for row in rows:
                if row:
                    self.CustomerTable.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"error due to {str(ex)}")

    def search(self):
        con = sqlite3.connect(database="bms.db")
        cur = con.cursor()
        try:
            if self.var_search.get() == "":
                messagebox.showerror("Error", "This field can't be empty", parent=self.root)
            cur.execute(f"select * from customer where customer_id=?", (self.var_search.get(),))
            row = cur.fetchone()
            print(row)
            if row != None:
                self.CustomerTable.delete(*self.CustomerTable.get_children())
                self.CustomerTable.insert('', END, values=row)
            else:
                messagebox.showerror("Error", "No Record Found", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"error due to {str(ex)}")

    def go_back_to_login(self):
        self.root.destroy()  # Close the dashboard window
        self.new_win = Tk()  # Create a new Tk instance for the login window
        self.new_obj = Loginn(self.new_win)  # Open the login window


if __name__ == "__main__":
    root = Tk()
    obj = CustomerClass(root, None)  # Pass None as the dashboard instance
    root.mainloop()