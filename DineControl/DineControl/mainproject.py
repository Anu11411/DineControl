# Author: Anupriya
# Date: June 18, 2023
# Description: This is a restaurant management app for "The Green Leaf - Vegetarian Indian Restaurant."
import tkinter as tk
from tkinter import ttk, messagebox
import time

class RestaurantManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1200x800")
        self.root.title("The Green Leaf - Vegetarian Indian Restaurant")
        self.setup_styles()
        self.create_widgets()

    def setup_styles(self):
        self.style = ttk.Style()
        self.style.configure('Title.TLabel', font=('Times New Roman', 36, 'bold'), foreground='#006400')  # Dark green title
        self.style.configure('Subtitle.TLabel', font=('Arial', 18), foreground='#4CAF50')
        self.style.configure('Menu.TCheckbutton', font=('Arial', 16), foreground='black', background='#FFFF00', anchor='w')
        self.style.configure('Calc.TButton', font=('Arial', 16, 'bold'), foreground='black', background='#FFD700', width=10)
        self.style.map('Calc.TButton', background=[('active', '#FFD700')])
        self.style.configure('Main.TButton', font=('Arial', 16, 'bold'), foreground='black', background='#388E3C', width=12)
        self.style.map('Main.TButton', background=[('active', '#1B5E20')])  # Darker shade of green, text color black

    def create_widgets(self):
        self.root.configure(background='#D3ECA7')  # Light green background

        # Header Frame
        header_frame = tk.Frame(self.root, bg='white', pady=20)
        header_frame.pack(fill='x')

        ttk.Label(header_frame, text="The Green Leaf - Vegetarian Indian Restaurant", style='Title.TLabel').pack()
        self.clock_label = ttk.Label(header_frame, font=('Arial', 18), foreground='#4CAF50')
        self.clock_label.pack()

        # Left Menu Frame
        menu_frame = tk.Frame(self.root, bd=10, relief=tk.RIDGE, padx=20, pady=20, bg='#D3ECA7')  # Light green background
        menu_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        ttk.Label(menu_frame, text="Menu", font=('Arial', 24, 'bold'), background='#FFA500').grid(row=0, column=0, columnspan=3, pady=10)

        # Define menu categories and items
        self.menu_items = {
            'Appetizers': ['Paneer Tikka', 'Samosa', 'Vegetable Pakora'],
            'Main Course': ['Paneer Butter Masala', 'Chole Bhature', 'Aloo Paratha', 'Palak Paneer', 'Veg Biryani'],
            'Beverages': ['Lassi', 'Masala Chai', 'Fresh Lime Soda'],
            'Desserts': ['Gulab Jamun', 'Rasgulla', 'Kulfi']
        }
        self.item_prices = {
            'Paneer Butter Masala': 150,
            'Chole Bhature': 100,
            'Aloo Paratha': 80,
            'Palak Paneer': 120,
            'Veg Biryani': 130,
            'Lassi': 50,
            'Paneer Tikka': 120,
            'Samosa': 50,
            'Vegetable Pakora': 70,
            'Masala Chai': 30,
            'Fresh Lime Soda': 40,
            'Gulab Jamun': 60,
            'Rasgulla': 50,
            'Kulfi': 80
        }

        self.menu_vars = {item: tk.IntVar() for category in self.menu_items.values() for item in category}

        row_idx = 1
        for category, items in self.menu_items.items():
            ttk.Label(menu_frame, text=category, font=('Arial', 18, 'bold'), background='#D3ECA7').grid(row=row_idx, column=0, pady=5, sticky='w')
            row_idx += 1
            for item in items:
                checkbutton = ttk.Checkbutton(menu_frame, text=item, variable=self.menu_vars[item], style='Menu.TCheckbutton')
                checkbutton.grid(row=row_idx, column=0, sticky='w')
                entry = ttk.Entry(menu_frame, textvariable=self.menu_vars[item], width=5)
                entry.grid(row=row_idx, column=1)
                row_idx += 1

        # Right Calculator Frame
        calculator_frame = tk.Frame(self.root, bd=10, relief=tk.RIDGE, padx=20, pady=20, bg='#D3ECA7')  # Light green background
        calculator_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.expression = tk.StringVar()
        entry_calculator = ttk.Entry(calculator_frame, font=('Arial', 20), textvariable=self.expression, justify='right')
        entry_calculator.grid(row=0, columnspan=4, padx=10, pady=10, sticky='we')

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('+', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('*', 3, 3),
            ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('/', 4, 3)
        ]

        for (text, row, column) in buttons:
            ttk.Button(calculator_frame, text=text, command=lambda t=text: self.on_button_click(t), style='Calc.TButton').grid(row=row, column=column, padx=5, pady=5)

        # Order Frame
        order_frame = tk.Frame(self.root, bd=10, relief=tk.RIDGE, bg='#D3ECA7')  # Light green background
        order_frame.pack(side=tk.BOTTOM, padx=20, pady=20, fill='both', expand=True)

        ttk.Label(order_frame, text="Order Details", font=('Arial', 24, 'bold')).pack()

        self.summary_text = tk.Text(order_frame, height=10, width=50, font=('Arial', 12))
        self.summary_text.pack(pady=10)

        # Reservation Frame
        reservation_frame = tk.Frame(self.root, bd=10, relief=tk.RIDGE, bg='#D3ECA7')  # Light green background
        reservation_frame.pack(side=tk.BOTTOM, padx=20, pady=20, fill='both', expand=True)

        ttk.Label(reservation_frame, text="Reservation", font=('Arial', 24, 'bold')).grid(row=0, columnspan=2, pady=10)

        ttk.Label(reservation_frame, text="Date:", font=('Arial', 16)).grid(row=1, column=0, padx=10, pady=5, sticky='e')
        self.date_entry = ttk.Entry(reservation_frame, font=('Arial', 16))
        self.date_entry.grid(row=1, column=1, padx=10, pady=5, sticky='w')

        ttk.Label(reservation_frame, text="Time:", font=('Arial', 16)).grid(row=2, column=0, padx=10, pady=5, sticky='e')
        self.time_entry = ttk.Entry(reservation_frame, font=('Arial', 16))
        self.time_entry.grid(row=2, column=1, padx=10, pady=5, sticky='w')

        ttk.Button(reservation_frame, text="Make Reservation", command=self.make_reservation, style='Main.TButton').grid(row=3, columnspan=2, pady=10)

        # Buttons
        button_frame = tk.Frame(self.root, bg='#D3ECA7')  # Light green background
        button_frame.pack(pady=20)

        ttk.Button(button_frame, text="Calculate Total", command=self.calculate_total, style='Main.TButton').pack(side=tk.LEFT, padx=10)
        ttk.Button(button_frame, text="Reset", command=self.reset, style='Main.TButton').pack(side=tk.LEFT, padx=10)
        ttk.Button(button_frame, text="Exit", command=self.root.destroy, style='Main.TButton').pack(side=tk.LEFT, padx=10)

        # Clock Update
        self.update_clock()

    def update_clock(self):
        current_time = time.strftime('%Y-%m-%d %H:%M:%S %p')
        self.clock_label.config(text=current_time)
        self.root.after(1000, self.update_clock)

    def on_button_click(self, char):
        if char == '=':
            try:
                result = str(eval(self.expression.get()))
                self.expression.set(result)
            except:
                self.expression.set("Error")
        elif char == 'C':
            self.expression.set("")
        else:
            current_expression = self.expression.get()
            self.expression.set(current_expression + str(char))

    def calculate_total(self):
        total_cost = 0
        order_summary = ""

        # Clear previous order summary
        self.summary_text.delete('1.0', tk.END)

        # Iterate through selected items
        for item, var in self.menu_vars.items():
            quantity = var.get()
            if quantity > 0:
                price = self.item_prices[item] * quantity
                total_cost += price
                order_summary += f"{item}: {quantity} x {self.item_prices[item]} = {price} INR\n"

        sgst = total_cost * 0.09
        cgst = total_cost * 0.09
        total_with_tax = total_cost + sgst + cgst

        order_summary += f"\nTotal Cost: {total_cost} INR"
        order_summary += f"\nSGST (9%): {sgst:.2f} INR"
        order_summary += f"\nCGST (9%): {cgst:.2f} INR"
        order_summary += f"\nTotal Cost with Taxes: {total_with_tax:.2f} INR"
        self.summary_text.insert(tk.END, order_summary)

    def make_reservation(self):
        date = self.date_entry.get()
        time_ = self.time_entry.get()
        if date and time_:
            messagebox.showinfo("Reservation", f"Reservation made for {date} at {time_}")
        else:
            messagebox.showwarning("Input Error", "Please enter both date and time")

    def reset(self):
        self.expression.set("")
        self.summary_text.delete('1.0', tk.END)
        self.date_entry.delete(0, tk.END)
        self.time_entry.delete(0, tk.END)
        for var in self.menu_vars.values():
            var.set(0)

if __name__ == "__main__":
    root = tk.Tk()
    app = RestaurantManagementApp(root)
    root.mainloop()
