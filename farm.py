import tkinter as tk
from tkinter import messagebox


app = tk.Tk()
app.title("Agri Mart -> Direct Market Access")
app.geometry("500x520")
app.configure(bg="#e8f5e9")

cart = {}
total = 0
payment_method = tk.StringVar()


page1 = tk.Frame(app, bg="#e8f5e9")
page2 = tk.Frame(app, bg="#e8f5e9")
page3 = tk.Frame(app, bg="#e8f5e9")

for frame in (page1, page2, page3):
    frame.place(x=0, y=0, width=520, height=600)

vegetables = {
    "Tomato 🍅": 30,
    "Potato 🥔": 25,
    "Onion 🧅": 40,
    "Carrot 🥕": 35,
    "Cabbage 🥬": 20
}
fruits = {
    "Apple 🍎": 50,
    "Banana 🍌": 40,
    "Orange 🍊": 35,
    "Mango 🥭": 60,
    "Grapes 🍇": 70
}
def show_page(frame):
    frame.tkraise()

def add_to_cart(item, price):
    global total
    cart[item] = cart.get(item, 0) + 1
    total += price
    messagebox.showinfo("Added", f"{item} added to cart")

def go_to_cart():
    cart_list.delete(0, tk.END)
    for item, qty in cart.items():
        cart_list.insert(tk.END, f"{item} x {qty}")
    total_label.config(text=f"Total: ₹{total}")
    show_page(page2)

def place_order():
    if not payment_method.get():
        messagebox.showwarning("Payment", "Select payment method")
        return
    show_page(page3)

def confirm_order():
    address = address_text.get("1.0", tk.END).strip()
    if address == "":
        messagebox.showwarning("Address", "Enter delivery address")
        return

    messagebox.showinfo(
        "Order Status",
        "🎉 Ordered Successfully!\n\nThank you for shopping with Agri Mart"
    )
    app.destroy()

tk.Label(page1, text="🥦 Vegetable Market",
         font=("Arial", 18, "bold"),
         bg="#2e7d32", fg="white", pady=10).pack(fill="x")

market_frame = tk.Frame(page1, bg="#e8f5e9")
market_frame.pack(pady=15)

for veg, price in vegetables.items():
    card = tk.Frame(market_frame, bg="white", bd=2, relief="ridge")
    card.pack(pady=6, padx=10, fill="x")

    tk.Label(card, text=veg, font=("Arial", 12, "bold"),
             bg="white").pack(side="left", padx=10)

    tk.Label(card, text=f"₹{price} / kg",
             font=("Arial", 11), bg="white").pack(side="left")

    tk.Button(card, text="Add",
              bg="#388e3c", fg="white",
              command=lambda v=veg, p=price: add_to_cart(v, p)
              ).pack(side="right", padx=10)


for fruits,price in fruits.items():
    card = tk.Frame(market_frame, bg="white", bd=4, relief="ridge")
    card.pack(pady=6, padx=10, fill="x")

    tk.Label(card, text=fruits, font=("Arial", 12, "bold"),
             bg="white").pack(side="left", padx=10)

    tk.Label(card, text=f"₹{price} / kg",
             font=("Arial", 11), bg="white").pack(side="left")

    tk.Button(card, text="Add",
              bg="#388e3c", fg="white",
              command=lambda v=fruits, p=price: add_to_cart(v, p)
              ).pack(side="right", padx=10)
tk.Button(page1, text="Go to Cart →",
          bg="#1b5e20", fg="white",
          font=("Arial", 12),
          command=go_to_cart).pack(pady=20)


tk.Label(page2, text="🛒 Cart & Payment",
         font=("Arial", 18, "bold"),
         bg="#2e7d32", fg="white", pady=10).pack(fill="x")

cart_list = tk.Listbox(page2, width=45, height=8)
cart_list.pack(pady=15)

total_label = tk.Label(page2, text="Total: ₹0",
                       font=("Arial", 14, "bold"),
                       bg="#e8f5e9")
total_label.pack(pady=5)

tk.Label(page2, text="Select Payment Method",
         font=("Arial", 13, "bold"),
         bg="#e8f5e9").pack(pady=10)

tk.Radiobutton(page2, text="GPay",
               variable=payment_method, value="GPay",
               bg="#e8f5e9", font=("Arial", 11)).pack()

tk.Radiobutton(page2, text="PhonePe",
               variable=payment_method, value="PhonePe",
               bg="#e8f5e9", font=("Arial", 11)).pack()

tk.Button(page2, text="Proceed to Address →",
          bg="#1b5e20", fg="white",
          font=("Arial", 12),
          command=place_order).pack(pady=20)


tk.Label(page3, text="🏠 Delivery Address",
         font=("Arial", 18, "bold"),
         bg="#2e7d32", fg="white", pady=10).pack(fill="x")

address_text = tk.Text(page3, width=45, height=8)
address_text.pack(pady=20)

tk.Button(page3, text="Confirm Order",
          bg="#388e3c", fg="white",
          font=("Arial", 13),
          command=confirm_order).pack(pady=20)


show_page(page1)
app.mainloop()
