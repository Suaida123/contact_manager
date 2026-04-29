import tkinter as tk
from tkinter import messagebox

# Dictionary to store contacts
contacts = {}

# Functions
def add_contact():
    name = entry_name.get().strip()
    phone = entry_phone.get().strip()
    email = entry_email.get().strip()

    if name == "" or phone == "" or email == "":
        messagebox.showwarning("Warning", "All fields are required!")
        return

    if name in contacts:
        messagebox.showwarning("Warning", "Contact already exists!")
    else:
        contacts[name] = {"phone": phone, "email": email}
        messagebox.showinfo("Success", "Contact added!")

    clear_fields()

def search_contact():
    name = entry_name.get().strip()

    if name in contacts:
        contact = contacts[name]
        result_var.set(f"Phone: {contact['phone']} | Email: {contact['email']}")
    else:
        result_var.set("Contact not found!")

def delete_contact():
    name = entry_name.get().strip()

    if name in contacts:
        del contacts[name]
        messagebox.showinfo("Success", "Contact deleted!")
        result_var.set("")
    else:
        messagebox.showwarning("Warning", "Contact not found!")

def display_contacts():
    if not contacts:
        result_var.set("No contacts available.")
        return

    all_contacts = ""
    for name, info in contacts.items():
        all_contacts += f"{name} - {info['phone']} - {info['email']}\n"

    result_var.set(all_contacts)

def clear_fields():
    entry_name.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_email.delete(0, tk.END)

# GUI Setup
root = tk.Tk()
root.title("Contact Management System")
root.geometry("400x400")

# Labels and Entries
tk.Label(root, text="Name").pack()
entry_name = tk.Entry(root)
entry_name.pack()

tk.Label(root, text="Phone").pack()
entry_phone = tk.Entry(root)
entry_phone.pack()

tk.Label(root, text="Email").pack()
entry_email = tk.Entry(root)
entry_email.pack()

# Buttons
tk.Button(root, text="Add Contact", command=add_contact).pack(pady=5)
tk.Button(root, text="Search Contact", command=search_contact).pack(pady=5)
tk.Button(root, text="Delete Contact", command=delete_contact).pack(pady=5)
tk.Button(root, text="Display All", command=display_contacts).pack(pady=5)

# Result Display
result_var = tk.StringVar()
tk.Label(root, textvariable=result_var, wraplength=350, justify="left").pack(pady=10)

# Run app
root.mainloop()