from logging import root
import tkinter as Tk
from tkinter import ttk,messagenox

class RestaurantOrderManagement:
    def __init__(self,root):
        self.root=root
        self.root.title("Restaurant Management App")
        self.menu_items={
            "Fries":2,
            "Lunch meal":2,
            "burger meal":3,
            "Pizza":4,
            "Chesse burger":3,
            "Drinks":1
        }

        self.exchange_rate=2
        self.setup_background(root)

    frame=ttk.Frame(root)
    frame.place(relx=0.5,rely=0.5,anchor=tk.CENTER)
    ttk.Label(frame,text="Restaurant Management App",font=("Arial",20)).grid(row=0,column=0,columnspan=3,pady=10,pady=10)

        self.menu_labels={}
        self.menu_quantities={}

        for i, (item ,price) in enumerate(self.menu_items.items(),start=1):
            label=ttk.Label(
                frame,
                text=f"{item} - ${price}",
                font=("Arial",12)
            )
            label.grid(row=i,column=0,pady=5,padx=5)
            self.menu_labels[item]=label

            quantity_entry=ttk.Entry(frame,width=5)
            quantity_entry.grid(row=i,column=1,pady=5,padx=5)
            self.menu_quantities[item]=quantity_entry

        self.currency_var=tk.StringVar()
    ttk.Label(frame,text="Select Currency:",font=("Arial",12)).grid(row=i+1,column=0,pady=5,padx=5)