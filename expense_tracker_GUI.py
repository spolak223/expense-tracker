#EXPENSE TRACKER GUI

import customtkinter as ctk
from expense_tracker import Tracker
import json
import tkinter.ttk as ttk
import os
import datetime as dt
import tkinter as tk


ctk.set_appearance_mode('Dark')
ctk.set_default_color_theme('blue')

app = ctk.CTk()

app.geometry('1000x800')
app.title("Expense Tracker")

class ExpenseTrackerApp:
    def __init__(self, tracker, app):
        self.tracker = tracker
        self.app = app

        self.expense_str = "expense tracker save.json"
        
        self.tabs = ctk.CTkTabview(master=app,
                                            width=850,
                                            height=650,
                                            fg_color="navy",
                                            state="normal")
        self.tabs.pack(pady=10)

        self.main_m_tab = self.tabs.add("Main Menu")

        self.main_menu_label = ctk.CTkLabel(master=self.main_m_tab, 
                                            text='Expense Tracker App')
        self.main_menu_label.pack()

        self.expense_name = ctk.CTkEntry(master=self.main_m_tab, 
                                         placeholder_text='Enter Expense Name..')
        self.expense_amount = ctk.CTkEntry(master=self.main_m_tab, 
                                           placeholder_text='Enter Expense Value..')
        self.expense_name.pack()
        self.expense_amount.pack()

        self.confirm_expense = ctk.CTkButton(master=self.main_m_tab, 
                                             command=self.add_expense, 
                                             text='Confirm')
        self.confirm_expense.pack(pady=10)

        self.error_lbl = ctk.CTkLabel(master=self.main_m_tab, text='', 
                                      text_color='red')
        self.error_lbl.pack()

        self.successfull_expense = ctk.CTkLabel(master=self.main_m_tab, 
                                                text='', 
                                                text_color='green')
        self.successfull_expense.pack()



        #view all expenses page

        self.view_expenses_tab = self.tabs.add("View expenses")

        self.sort_box = ctk.CTkComboBox(master=self.view_expenses_tab, 
                                        values=['Name Asc', 'Name Desc', "Amount Asc", "Amount Desc", "Date Asc", "Date Desc"],
                                        variable=ctk.StringVar(value="Sort By"),
                                        command=self.sort_tracker)
        
        self.sort_box.bind("<<ComboboxSelected>>", self.sort_tracker)
        
        self.sort_box.pack(padx=0, pady=10)
        

        style = ttk.Style()
        style.configure("Treeview", font=("Sogoe UI", 16), rowheight=30.5)
        style.configure("Treeview.Heading", font=("Segoe UI", 19))
        style.configure("")

        self.treeview = ttk.Treeview(self.view_expenses_tab, 
                                columns=("Item", "Amount", "Date", "ID"),
                                show="headings")
        self.treeview.heading("Item", text="Expense")
        self.treeview.heading("Amount", text="Amount")
        self.treeview.heading("Date", text="Date")
        self.treeview.heading("ID", text="ID")
        
                
        self.treeview.pack(expand=True, fill=ctk.BOTH)
        for i in self.tracker.expenses:
            self.treeview.insert("", "end", values=(i['item'], i['amount'], i['date'], i['id']))

        


        self.delete_expense_btn = ctk.CTkButton(master=self.view_expenses_tab, text='Delete expense', command=self.delete_item)
        self.delete_expense_btn.pack(pady=10, side=tk.LEFT)
        
        
        self.treeview.bind("<ButtonRelease-1>", self.get_item)
        


        
        
        
        


        
        

    def add_expense(self):
        
        try:
            
            if float(self.expense_amount.get()) > 0 and not self.expense_name.get().isnumeric():
                
                self.error_lbl.configure(text='')
                self.tracker.new_expense(self.expense_name.get(),  
                                        float(self.expense_amount.get()))
                self.successfull_expense.configure(text=self.tracker.added_expense_msg)
                self.successfull_expense.after(1000, lambda: self.successfull_expense.configure(text=''))
                self.date = dt.datetime.now().strftime("%d/%m/%Y")
                self.treeview.insert("", "end", values=(self.expense_name.get().capitalize(), self.expense_amount.get(), self.date, self.tracker.id))
                self.expense_name.delete(0, ctk.END)
                self.expense_amount.delete(0, ctk.END)
                self.tracker.save_program()
                
            else:
                self.error_lbl.configure(text='Invalid expense name or value inputted!')
                self.confirm_expense.configure(state='disabled')
                self.error_lbl.after(800, lambda: self.error_lbl.configure(text=''))
                self.confirm_expense.after(800, lambda: self.confirm_expense.configure(state='normal'))
                
                return 
                
                
        except ValueError:
            self.error_lbl.configure(text='Invalid input!')
            self.confirm_expense.configure(state='disabled')
            self.error_lbl.after(500, lambda: self.error_lbl.configure(text=''))
            self.confirm_expense.after(500, lambda: self.confirm_expense.configure(state='normal'))
        
        


        
    
    def save_tracker(self):
        self.tracker.save_program()
        self.save_confirm.configure(text='Saved Program!')
        self.save_confirm.after(800, lambda: self.save_confirm.configure(text=""))
    
    
    def sort_tracker(self, event=None):
        selected = self.sort_box.get()
        print(selected)
        self.tracker.sort_expenses(selected)
        self.refresh_tree()



    def get_item(self, event=None):
        self.select = self.treeview.focus()
        return self.treeview.item(self.select)['values']
    
    def delete_item(self, event=None):
        items_dlt = self.get_item()
        selected_item = self.treeview.selection()[0]
        if selected_item:
            

            self.treeview.delete(selected_item)
            self.tracker.delete_expense(items_dlt)
        self.refresh_tree()
    
    def refresh_tree(self):
        for i in self.treeview.get_children():
            self.treeview.delete(i)

        for i in self.tracker.expenses:
            self.treeview.insert("", "end", values=(i['item'], i['amount'], i['date'], i['id']))
                



        

        
        
    
        
        
            


        
tracker = Tracker()
expense = ExpenseTrackerApp(tracker, app)
app.mainloop()


