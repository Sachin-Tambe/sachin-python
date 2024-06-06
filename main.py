import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk 
class hotel_managment:
    def __init__(self):
        self.R_N = ''
        self.R_M = {}
        self.restaurent_image = None
        self.tk_image =None
        self.image_label =None
        self.selected_item = {}
        self.order_bill = 0

    def read_details_from_file_launch(self,file_path):
        with open(file_path , 'r') as file :
            lines = file.readlines()
        for line in lines :
            parts =  line.strip().split(',')
            self.R_N = parts[0].strip()
            self.R_M = eval(','.join(parts[1:]))
    def set_image(self,Image_path):
        self.restaurent_image = Image.open(Image_path)
        self.restaurent_image = self.restaurent_image.resize((200,200))
        self.tk_image = ImageTk.PhotoImage(self.restaurent_image)
        self.image_label = tk.Label(window, image=self.tk_image ).place(x=650 , y=100)
    def create_button_launch(self):
        self.new_window = tk.Tk()
        self.new_window.title("Launch Window")
        self.new_window.geometry('500x500')
        
        y_position = 130
        for item, price in self.R_M.items():
            cd = tk.Label(self.new_window , text=f"{item} -₹{price}")
            cd.place(x=200,y=y_position)
            entry_var = tk.IntVar()
            entry = tk.Entry(self.new_window , textvariable=entry_var)
            entry.place(x=300 ,y=y_position)
            self.selected_item[item]=entry_var
            y_position += 30
        confirm_button = tk.Button(new_window, text='Confirm' , command=self.confirm_order)
        confirm_button.place(x=200 , y=y_position+10) 

    def confirm_order(self):
        current_order_bill = 0
        for item, (price, entry_var) in self.selected_item.items():
            quantity = entry_var.get()
            current_order_bill += price * quantity 
            print(f"{item}: {quantity} x ₹{price} = ₹{price * quantity}")

        self.total_bill += current_order_bill
        more_order = messagebox.askyesno("More Orders Do you want to order more items?")
        if not more_order :
            self.new_window.destroy() 

rest = hotel_managment()
rest.read_details_from_file_launch(r'C:\Users\sachi\OneDrive\Desktop\sachin python\details.txt')
restaurent_name = rest.R_N
restaurent_menu = rest.R_M

window = tk.Tk()
window.title(restaurent_name)
window.geometry('500x500')
title_label = tk.Label(window,text=restaurent_name.title(), font=('Helvetica',22)).place(x=650,y=310)

rest.set_image(r"C:\Users\sachi\OneDrive\Desktop\sachin python\iam.png")
launch_button = tk.Button(window,text="View launch Menu" , command=rest.create_button_launch)
launch_button.place(height=50 , width=200 ,x=650 , y=500 )
window.mainloop()

