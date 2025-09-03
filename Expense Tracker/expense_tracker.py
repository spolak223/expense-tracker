#EXPENSE TRACKER
from pathlib import Path
import json
import os
from algs import display
import datetime as dt
import datetime as datetime



class Tracker:
    def __init__(self):
        
        self.T = []
        self.expense_str = "expense_tracker_save.json"
        with open(self.expense_str, "r") as file:
            if os.path.getsize(self.expense_str) > 0:
                data = json.load(file)
                self.expenses = data['my_list']
                if len(data['my_list']) == 0:
                    self.id = 0
                elif len(data['my_list']) == 1:
                    self.id = data['my_list'][-1]['id']
                else:
                    self.id = data['my_list'][-1]['id']
            else:
                self.expenses = []
                self.id = 0
        
    
    def new_expense(self, name, amount):
        """Adds new expense to tracker"""
        if amount != 0 and amount > 0:
            if self.id == 0:
                self.id += 1
                self.new_expenses = {'item' : name.capitalize(), 'amount' : float(amount), 'date': dt.datetime.now().strftime('%d/%m/%Y'), 'id' : self.id}
                self.expenses.append(self.new_expenses)
                self.added_expense_msg = f"Successfully added: {name.capitalize()} -> £{amount:.2f} on {self.new_expenses['date']}\n"
                
            else:
                with open(self.expense_str, "r") as file:
                    data = json.load(file)
                    if data['my_list']:
                        self.id = data['my_list'][-1]['id'] + 1
                        self.new_expenses = {'item' : name.capitalize(), 'amount' : float(amount), 'date': dt.datetime.now().strftime('%d/%m/%Y'), 'id' : self.id}
                        self.expenses.append(self.new_expenses)
                        self.added_expense_msg = f"Successfully added: {name.capitalize()} -> £{amount:.2f} on {self.new_expenses['date']}\n"
                    else:
                        self.id = 0
            
            #return self.added_expense_msg
        else:
            print("The number you are trying to enter is either 0 or less than 0!")
            return None
        
    
    def delete_expense(self, id_remv):
        with open(self.expense_str, "r+") as file:
            data = json.load(file)
            if id_remv[3]:
                for key, i in enumerate(data['my_list']):
                    if id_remv[3] == i['id']:
                        data['my_list'][key].pop('item')
                        data['my_list'][key].pop('amount')
                        data['my_list'][key].pop('date')
                        data['my_list'][key].pop('id')
                        for j in data['my_list']:
                            if not j:
                                data['my_list'].remove(j)
            #if len(data['my_list']) == 0:
            #        self.id = 0
            #else:
            #    self.id = data['my_list'][-1]['id']
            

        with open(self.expense_str, "w") as file:
            if data:
                self.edit_id(id_remv)
                for key, i in enumerate(self.expenses):
                    if id_remv[3] == i['id']:
                        self.expenses.pop(key)
                json.dump({'my_list' : self.expenses}, file, indent=2)
    
    def edit_id(self, id_remv):
        for i in self.expenses:
            if i['id'] > id_remv[3]:
                i['id'] -= 1
            elif i['id'] == 1:
                self.id = 0
    

    def sort_expenses(self, selected):

        sort_map = {
            "Name Asc" : ("item", False),
            "Name Desc" : ("item", True),
            "Amount Asc" : ("amount", False),
            "Amount Desc" : ("amount", True),
            "Date Asc" : ("date", False),
            "Date Desc" : ("date", True)
        }
        if selected == "Date Asc":
            for key in range(len(self.expenses)):
                date = self.expenses[key]['date']
                date = date.split("/")
                self.expenses = sorted(self.expenses, key=lambda x: dt.datetime.strptime(x["date"], "%d/%m/%Y"), reverse=False)
            return self.expenses
        elif selected == "Date Desc":
            for key in range(len(self.expenses)):
                date = self.expenses[key]['date']
                date = date.split("/")
                self.expenses = sorted(self.expenses,  key=lambda x: dt.datetime.strptime(x["date"], "%d/%m/%Y"), reverse=True)
            return self.expenses
        else:
                

            key, reverse = sort_map[selected]
            self.expenses = sorted(self.expenses, key=lambda x: x[key], reverse=reverse)
            return self.expenses

        



        
    
    def all_expenses(self):
        """Displays all expenses"""
        print("///EXPENSES///")
        if self.expenses:
            for item in self.expenses:
                print(f"> {item['item']}: £{item['amount']:.2f}")
        else:
            print("Nothing here...\n")
        print("\n")
    
    def view_total(self):
        total = 0
        for items in self.expenses:
            total += items['amount']
        return total
    
    def save_program(self):
        self.new_dict = {'my_list' : self.expenses}
        if os.path.getsize(self.expense_str) > 0:
            with open(self.expense_str, "r") as file:
                data = json.load(file)
                #self.expenses = data['my_list']
                
            with open(self.expense_str, "w") as file:
                json.dump({'my_list' : self.expenses}, file, indent=2)
                print(f"saved the following: {self.expenses}")

                

            

                
        else:
            with open(self.expense_str, "w") as file:
                json.dump(self.new_dict, file, indent=2)
        


            
            

        return "Successfully saved!\n"
    

    
    def load_program(self):
        file_path = Path(self.expense_str)
        if file_path.exists():
            with open(self.expense_str, "r") as file:
                data = json.load(file)
                self.expenses = data
                print("Successfully loaded previous expense tracker!\n")
        else:
            return print("no previous save found!\n")
        return self.expenses
    
    def delete_saved_file(self):
        if os.path.exists(self.expense_str):
            os.remove(self.expense_str)
            print("Save file has been deleted!\n")
        else:
            print("No file has been found to delete!\n")
        
    
    
    def update_T(self):
        self.T.clear()
        if self.expenses:
            for item in self.expenses:
                self.T.append(item['item'])

    
    def refresh(self):
        open("expense tracker save.json", "w").close()
        print("refreshed")
        return
                

tracker = Tracker()
