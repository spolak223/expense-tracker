import sqlite3
from datetime import datetime


connection = sqlite3.connect(r'c:/Users/spola/OneDrive/Documenten/Python Projects/tracker.db')

crsr = connection.cursor()



class HabitTracker:
    def __init__(self):
        self.habits = {}
        self.today = datetime.today()
        with open("Primary Keys.txt", "r") as file:
            for i in file.readlines():
                self.pk = int(i)
            file.close()
        

    def menu(self):
        """Allows the user to decide what to do"""
        print("//"*20)
        print("1. Add a new habit to your habit tracker")
        print("2. View all your current habits")
        print("3. Delete a habit from your habit tracker")
        print("4. Order your habits and display them")
        print("5. Log down a habit to update its streak")
        print("6. Exit")
        print("//"*20)
        print("\n")
    
    def convert_user_habit_input(self, habit):
        habit = habit.lower().strip().replace(",", "").replace(".", "").replace("!", "").replace("?", "")
        return habit


    def add_new(self, habit):
        habit = self.convert_user_habit_input(habit)
        if habit in self.habits.keys():
            print("Habit is already in habit tracker!")
            return None
        else:
            self.habits[habit] = [1, self.today.strftime("%Y-%m-%d"), self.pk]
            self.pk += 1
            print("//"*20)
            print(f"Successfully added in new habit of {habit.capitalize()} on {self.today.strftime("%d/%m/%Y")}!")
            print("//"*20)
            print("\n")
            return self.habits
    
    def log_down(self, habit):
        habit = self.convert_user_habit_input(habit)
        try:
            if habit not in self.habits.keys():
                print("No habit under that name was found")
            else:
                self.habits[habit][0] += 1
                print(f"Habit of {habit.capitalize()} has now a streak of {self.habits[habit][0]} and updated on {self.today.strftime("%d/%m/%Y")}!")
        except (KeyError, ValueError):
            print("Attempting to access value not in habit tracker!")


    def delete_task(self):
        pass

    def order_by(self):
        pass


#idea for primary key generataion -> update it in the game loop, however, when game loop is exited, then save the current primary key to text file and move on from there
        


tracker = HabitTracker()
tracker.menu()
tracker.add_new("Working out")
tracker.log_down("working out")
tracker.add_new("gooning out")
tracker.add_new("MeDiTaTing!")
tracker.log_down("mediTating?!")
print(tracker.habits)

table = """CREATE TABLE habits (
habit_id INTEGER PRIMARY KEY,
habit_name VARHCAR(20),
streak INTEGER,
date_logged DATE);"""


connection.close()



