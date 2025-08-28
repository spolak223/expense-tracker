import customtkinter as ctk
import Expense Tracker as 

ctk.set_appearance_mode('Dark')
ctk.set_default_color_theme('blue')

app = ctk.CTk()

app.geometry('600x400')
app.title("Expense Tracker")

class ExpenseTrackerApp:
    def __init__(self, tracker):
        super().__init__()
        self.tracker = tracker
    
        self.main_menu = ctk.CTkFrame(master=app)
        self.main_menu.pack(padx=20, pady=20, fill='both', expand=True)



expenseApp = ExpenseTrackerApp(tracker)

app.mainloop()
