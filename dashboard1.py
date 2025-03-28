from tkinter import *
import tkinter
from PIL import Image, ImageTk
from customer import CustomerClass
from loginn import Loginn
from viewresult import view_result_class  # Import the Loginn class
from studentt import CustomerClassPayment


class RMS:
    def __init__(self, root):
        self.root = root
        # Background property
        self.root.title("श्री समर्थ कृपा एंटरप्रायझेस")
        self.root.geometry("1366x740")
        self.root.resizable(False, False)
        self.bg_img = Image.open("images/bglogin.jpg")
        self.bg_img = self.bg_img.resize((1500, 900))
        self.bg_img = ImageTk.PhotoImage(self.bg_img)
        self.lab_bg = Label(self.root, image=self.bg_img).place(x=1, y=1, width=1500, height=950)

        # Title
        title = Label(self.root, text="श्री समर्थ कृपा एंटरप्रायझेस", padx=20, compound=LEFT,
                      font=("Time new romes", 20, "bold"), bg="lightblue", fg="white").place(x=0, y=1, relwidth=1, height=50)

        # Buttons
        btn_customerpayment = Button(self.root, text="Add New Customer Information", font=("goudy old style", 25, "bold"), bg="#F0F8FF",
                           fg="black", cursor="hand2", command=self.add_customer).place(x=20, y=180, width=500, height=65)
        btn_customer_info = Button(self.root, text="Customer Information", font=("goudy old style", 25, "bold"), bg="#F0F8FF",
                           fg="black", cursor="hand2", command=self.add_customerpayment).place(x=20, y=320, width=330, height=65)
        btn_viewcustinfo = Button(self.root, text="View payment details of customer", font=("goudy old style", 25, "bold"), bg="#F0F8FF",
                           fg="black", cursor="hand2", command=self.pdf).place(x=20, y=450, width=500, height=65)
       
        # Exit Button
        exit_btn = Button(self.root, text="Exit", font=("Times new romen", 14), fg="black", bg="red", cursor="hand2",
                           command=self.iExit).place(x=1260, y=650, width=100, height=38)

        # Back Button
        back_btn = Button(self.root, text="Back to Login", font=("Times new roman", 14), fg="black", bg="lightgray", cursor="hand2",
                          command=self.go_back_to_login).place(x=20, y=650, width=150, height=38)

    # Exit the application with confirmation
    def iExit(self):
        iExit = tkinter.messagebox.askyesno("RMS", "Do you want to exit?", parent=self.root)
        if iExit > 0:
            self.root.destroy()
            return

    # Go back to the login screen with confirmation
    def go_back_to_login(self):
        confirm = tkinter.messagebox.askyesno("RMS", "Are you sure you want to go back to the login screen?", parent=self.root)
        if confirm:
            self.root.destroy()  # Close the dashboard window
            self.new_win = Tk()  # Create a new Tk instance for the login window
            self.new_obj = Loginn(self.new_win)  # Open the login window

    # Open the Customer Payment window
    def add_customerpayment(self):
        confirm = tkinter.messagebox.askyesno("RMS", "Are you sure you want to open the Customer Payment window?", parent=self.root)
        if confirm:
            self.new_win = Toplevel(self.root)  # Create a new Toplevel window
            self.new_obj = CustomerClassPayment(self.new_win)  # Open the CustomerClassPayment window

    # Open the Add Customer window
    def add_customer(self):
        confirm = tkinter.messagebox.askyesno("RMS", "Are you sure you want to open the Add Customer window?", parent=self.root)
        if confirm:
            self.new_win = Toplevel(self.root)  # Create a new Toplevel window
            self.new_obj = CustomerClass(self.new_win, self)  # Open the CustomerClass window

    # Open the View Payment Details window
    def pdf(self):
        confirm = tkinter.messagebox.askyesno("RMS", "Are you sure you want to open the View Payment Details window?", parent=self.root)
        if confirm:
            self.new_win = Toplevel(self.root)  # Create a new Toplevel window
            self.new_obj = view_result_class(self.new_win)  # Open the view_result_class window


if __name__ == "__main__":
    root = Tk()
    obj = RMS(root)
    root.mainloop()