import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3
import matplotlib.pyplot as plt
from datetime import datetime

class BMITrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced BMI Tracker")
        self.root.geometry('500x500')
        
     
        self.conn = sqlite3.connect('bmi_data.db')
        self.create_table()
        self.ll = tk.Label(root,text='Advanced BMI Tracker',font='arial 20 bold').pack(pady=(50,0))
        self.frm = tk.Frame(self.root)
        
        self.hero = tk.Frame(self.frm)
        tk.Label(self.hero,font='arial 15 bold', text="Weight (kg):").pack(side='left')
        self.weight_entry = tk.Entry(self.hero,font='arial 15',width=55)
        self.weight_entry.pack()
        self.hero.pack(fill='x',pady=5)
        
        self.second = tk.Frame(self.frm)
        tk.Label(self.second,font='arial 15 bold', text="Height (m):").pack(side='left')
        self.height_entry = tk.Entry(self.second,font='arial 15',width=55)
        self.height_entry.pack()
        self.second.pack(fill='x',pady=5)
        
        self.btnFrem = tk.Frame(self.frm)
        tk.Button(self.btnFrem, text="Calculate & Save",bg='lightgreen',width=30, command=self.calculate).pack(side='left')
        tk.Button(self.btnFrem, text="View History Graph",bg='lightgreen',width=30, command=self.show_graph).pack()
        
        self.btnFrem.pack(fill='x',pady=5)
        
     
        self.result_label = tk.Label(self.frm,font='arial 15 bold', text="Result: --")
        self.result_label.pack(pady=20)
        
        self.frm.pack(fill='both',expand=True,pady=50,padx=50)
        
    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS history
                          (date TEXT, bmi REAL)''')
        self.conn.commit()

    def calculate(self):
        try:
            w = float(self.weight_entry.get())
            h = float(self.height_entry.get())
            
            if w <= 0 or h <= 0: raise ValueError
            
            bmi = round(w / (h ** 2), 2)
            
            # Save to DB
            cursor = self.conn.cursor()
            cursor.execute("INSERT INTO history (date, bmi) VALUES (?, ?)", 
                           (datetime.now().strftime("%Y-%m-%d %H:%M:%S"), bmi))
            self.conn.commit()
            
            self.result_label.config(text=f"BMI: {bmi}")
            
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid positive numbers.")

    def show_graph(self):
        
        cursor = self.conn.cursor()
        cursor.execute("SELECT rowid, bmi FROM history")
        data = cursor.fetchall()
        
        if not data:
            messagebox.showinfo("Info", "No data to visualize yet.")
            return

       
        ids = [x[0] for x in data]
        bmis = [x[1] for x in data]
        
        plt.plot(ids, bmis, marker='o')
        plt.title("BMI Trend Over Time")
        plt.xlabel("Entry Number")
        plt.ylabel("BMI")
        plt.axhline(y=25, color='r', linestyle='-', label='Overweight Threshold')
        plt.axhline(y=18.5, color='y', linestyle='-', label='Underweight Threshold')
        plt.legend()
        plt.show()

if __name__ == "__main__":
    root = tk.Tk()
    app = BMITrackerApp(root)
    root.mainloop()
