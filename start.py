import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

class HotelManagement:
    def __init__(self):
        self.R_N = ''
        self.R_M = {}
        self.selected_items = {}
        self.overall_bill = 0

    def read_details_from_file_launch(self, file_path):
        with open(file_path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                parts = line.strip().split(',')
                self.R_N = parts[0].strip()
                self.R_M = eval(','.join(parts[1:]))

    def set_image(self, image_path):
        self.restaurent_image = Image.open(image_path)
        self.restaurent_image = self.restaurent_image.resize((200, 200))
        self.tk_image = ImageTk.PhotoImage(self.restaurent_image)

    def create_button_launch(self):
        new_window = tk.Toplevel()
        new_window.title("Launch Window")
        new_window.geometry('500x500')

        y_position = 130
        for item, price in self.R_M.items():
            label = tk.Label(new_window, text=f"{item} - ₹{price}")
            label.place(x=100, y=y_position)

            entry_var = tk.IntVar()
            entry = tk.Entry(new_window, textvariable=entry_var)
            entry.place(x=300, y=y_position)

            self.selected_items[item] = (price, entry_var)
            y_position += 30

        confirm_button = tk.Button(new_window, text="Confirm", command=self.confirm_order)
        confirm_button.place(x=200, y=y_position+30)

    def generate_bill_pdf(items, total_bill):
        # Create a PDF file
        file_path = "bill.pdf"
        c = canvas.Canvas(file_path, pagesize=letter)

        # Add content to the PDF
        c.setFont("Helvetica-Bold", 16)
        c.drawString(100, 750, "Invoice")
        c.drawString(100, 730, "-------")

        c.setFont("Helvetica", 12)
        y_position = 700
        for item, price in items.items():
            c.drawString(100, y_position, f"{item}: ₹{price}")
            y_position -= 20

        # Add total bill
        c.drawString(100, y_position, f"Total: ₹{total_bill}")

        # Save the PDF file
        c.save()
        print(f"Bill generated successfully: {file_path}")

        # Open the PDF file after generatingA
        os.startfile(file_path)

    # Example usage
    items = {
        "Item 1": 100,
        "Item 2": 200,
        "Item 3": 150
    }
    total_bill = sum(items.values())

    generate_bill_pdf(items, total_bill)
    def confirm_order(self):
        order_bill = 0
        for item, (price, entry_var) in self.selected_items.items():
            quantity = entry_var.get()
            order_bill += price * quantity
            print(f"{item}: {quantity} x ₹{price} = ₹{price * quantity}")

        more_order = messagebox.askyesno("More Orders", "Do you want to order more items?")
        if not more_order:
            print(f"Order Bill: ₹{order_bill}")
            self.overall_bill += order_bill  # Update overall_bill with order_bill
            print(f"Overall Bill: ₹{self.overall_bill}")
            generate_bill = messagebox.askyesno("Generate Bill", "Do you want to generate the bill?")
            if generate_bill:
                self.generate_bill_pdf(self.overall_bill)
                # Clear selected_items dictionary after generating bill
                self.selected_items.clear()

rest = HotelManagement()
rest.read_details_from_file_launch(r'C:\Users\sachi\OneDrive\Desktop\sachin python\details.txt')

window = tk.Tk()
window.title(rest.R_N)
window.geometry('900x700')

title_label = tk.Label(window, text=rest.R_N.title(), font=('Helvetica', 22))
title_label.place(x=650, y=310)

rest.set_image(r"C:\Users\sachi\OneDrive\Desktop\sachin python\iam.png")
image_label = tk.Label(window, image=rest.tk_image)
image_label.place(x=650, y=100)

launch_button_main_window = tk.Button(window, text="View Launch Menu", command=rest.create_button_launch)
launch_button_main_window.place(height=50, width=200, x=650, y=500)

window.mainloop()
