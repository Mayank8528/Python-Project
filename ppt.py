import tkinter as tk
from tkinter import messagebox

class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - ${self.price:.2f}"


class Order:
    def __init__(self, order_number):
        self.order_number = order_number
        self.items = []
        self.total_price = 0.0

    def add_item(self, menu_item, quantity):
        """Add item to the order."""
        self.items.append((menu_item, quantity))
        self.total_price += menu_item.price * quantity

    def display_order(self):
        """Display the current order details."""
        order_details = f"\nOrder Number: {self.order_number}\n"
        for item, quantity in self.items:
            order_details += f"- {item.name} x {quantity} - ${item.price * quantity:.2f}\n"
        order_details += f"Total Price: ${self.total_price:.2f}"
        return order_details
    
    def generate_final_bill(self, tax_rate=0.05, discount=0.0):
        """Generate the final bill with taxes and optional discount."""
        tax_amount = self.total_price * tax_rate
        discount_amount = self.total_price * discount
        final_amount = self.total_price + tax_amount - discount_amount
        
        bill_details = "\n--- Final Bill ---\n"
        for item, quantity in self.items:
            bill_details += f"{item.name} x {quantity} - ${item.price * quantity:.2f}\n"
        bill_details += f"Subtotal: ${self.total_price:.2f}\n"
        bill_details += f"Tax ({tax_rate * 100}%): ${tax_amount:.2f}\n"
        bill_details += f"Discount: -${discount_amount:.2f}" if discount_amount > 0 else "Discount: $0.00\n"
        bill_details += f"Total Amount: ${final_amount:.2f}"
        return bill_details


class Restaurant:
    def __init__(self, root):
        self.root = root
        self.menu = []
        self.orders = []
        self.current_order_number = 1

        self.order = None

        self.create_widgets()

    def add_menu_item(self, name, price):
        """Add items to the restaurant menu."""
        menu_item = MenuItem(name, price)
        self.menu.append(menu_item)

    def create_widgets(self):
        """Create the GUI widgets."""
        self.root.title("Restaurant Management System")
        
        # Set font size for the entire window
        self.font = ('Arial', 14)  # Adjust the font size for labels and buttons

        # Frame for menu items
        self.menu_frame = tk.Frame(self.root)
        self.menu_frame.pack()

        # Frame for the order details and final bill
        self.order_frame = tk.Frame(self.root)
        self.order_frame.pack()

        self.final_bill_frame = tk.Frame(self.root)
        self.final_bill_frame.pack()

        # Add menu items to the list
        self.add_menu_item("Burger", 5.99)
        self.add_menu_item("Pizza", 8.49)
        self.add_menu_item("Pasta", 7.99)
        self.add_menu_item("Salad", 4.49)

        # Display the menu
        self.display_menu()

    def display_menu(self):
        """Display menu items as buttons and quantity input fields."""
        self.clear_menu_frame()

        self.order = Order(self.current_order_number)
        
        for index, item in enumerate(self.menu, start=1):
            menu_item_frame = tk.Frame(self.menu_frame)
            menu_item_frame.pack()

            # Label for menu item with larger font
            label = tk.Label(menu_item_frame, text=f"{item.name} - ${item.price:.2f}", font=self.font)
            label.pack(side=tk.LEFT)

            # Entry for quantity with larger font
            quantity_entry = tk.Entry(menu_item_frame, font=self.font)
            quantity_entry.pack(side=tk.LEFT)
            quantity_entry.insert(0, "1")  # Default quantity is 1

            # Add to order button with larger font
            add_button = tk.Button(menu_item_frame, text="Add to Order", font=self.font,
                                   command=lambda item=item, entry=quantity_entry: self.add_to_order(item, entry))
            add_button.pack(side=tk.LEFT)

    def add_to_order(self, item, quantity_entry):
        """Add selected item and quantity to the order."""
        try:
            quantity = int(quantity_entry.get())
            if quantity > 0:
                self.order.add_item(item, quantity)
                messagebox.showinfo("Item Added", f"{item.name} x {quantity} added to your order.")
            else:
                messagebox.showerror("Invalid Input", "Quantity must be a positive number.")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid quantity.")

    def clear_menu_frame(self):
        """Clear the menu frame to refresh the display."""
        for widget in self.menu_frame.winfo_children():
            widget.destroy()

    def finalize_order(self):
        """Finalize the order and display the final bill."""
        if self.order.items:
            bill = self.order.generate_final_bill()
            self.show_final_bill(bill)
        else:
            messagebox.showerror("Empty Order", "You have not added any items to the order.")

    def show_final_bill(self, bill):
        """Display the final bill in the UI."""
        self.clear_final_bill_frame()
        final_bill_label = tk.Label(self.final_bill_frame, text=bill, font=self.font, justify=tk.LEFT)
        final_bill_label.pack()

    def clear_final_bill_frame(self):
        """Clear the final bill frame before displaying the new bill."""
        for widget in self.final_bill_frame.winfo_children():
            widget.destroy()

    def finish_order(self):
        """Finish the order and reset for a new one."""
        self.orders.append(self.order)
        self.current_order_number += 1
        self.display_menu()


# Initialize the Tkinter window and run the restaurant system
root = tk.Tk()
restaurant = Restaurant(root)

# Finalize order button with larger font
finish_button = tk.Button(root, text="Finalize Order", font=('Arial', 16), command=restaurant.finalize_order)
finish_button.pack()

# Start new order button with larger font
new_order_button = tk.Button(root, text="Start New Order", font=('Arial', 16), command=restaurant.finish_order)
new_order_button.pack()

root.mainloop()
