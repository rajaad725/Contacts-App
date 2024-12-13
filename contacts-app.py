import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk

class Person:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email
        
    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}"

class ContactsApp: 
    def __init__(self, root):
        self.root = root
        self.root.title("Contacts App")
        self.root.geometry("800x600")
        self.root.minsize(800, 600) # Minimum size to avoid layout breakage
        
        # Load and set the backgroud image
        self.bg_image_path = "background.jpg"
        self.bg_image = Image.open("background.jpg")
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)
        
        # Create a Canvas to hold the background image
        self.canvas = tk.Canvas(root, width=800, height=600)
        self.canvas.place(x=0, y=0, relwidth=1, relheight=1)
        
        # Set the Background Image to Canvas
        self.bg_image_on_canvas = self.canvas.create_image(0, 0, image=self.bg_photo, anchor="nw")
        
        # Bind resizing event to adjust the background image
        self.root.bind("<Configure>", self.resize_background)
        
        # Contacts Dictionary
        self.contacts = {}
        
        # Title Label
        self.title_label = tk.Label(root, text="Contacts App", font=("Helvetica", 24, "bold"), fg="white", bg="#5C6BC0")
        self.title_label.place(relx=0.5, rely=0.05, anchor="center")
        
        # Input Frame
        self.input_frame = tk.Frame(root, bg="#06BDFF", bd=5)
        self.input_frame.place(relx=0.5, rely= 0.2, relwidth=0.9, relheight=0.2, anchor="center")
        
        tk.Label(self.input_frame, text="Name:", font=("Arial", 14), bg="#06BDFF").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.name_entry = tk.Entry(self.input_frame, font=("Arial", 14))
        self.name_entry.grid(row=0, column=1, padx=10, pady=5, sticky="we")
        
        tk.Label(self.input_frame, text="Phone:", font=("Arial", 14), bg="#06BDFF").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.phone_entry = tk.Entry(self.input_frame, font=("Arial", 14))
        self.phone_entry.grid(row=1, column=1, padx=10, pady=5, sticky="we")
        
        tk.Label(self.input_frame, text="Email:", font=("Arial", 14), bg="#06BDFF").grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.email_entry = tk.Entry(self.input_frame, font=("Arial", 14))
        self.email_entry.grid(row=2, column=1, padx=10, pady=5, sticky="we")
        
        # Adjust Column and Row Weight for Resizing
        self.input_frame.columnconfigure(1, weight=1)
        
        # Button Frame
        self.button_frame = tk.Frame(root, bg="#06BDFF", bd=5)
        self.button_frame.place(relx=0.5, rely=0.45, relwidth=0.9, relheight=0.1, anchor="center")
        
        self.add_button = tk.Button(self.button_frame, text="Add/Update Contact", font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", command=self.add_or_update_contact)
        self.add_button.pack(side="left", expand=True, padx=10)
        
        self.clear_button = tk.Button(self.button_frame, text="Clear Fields", font=("Arial", 12, "bold"), bg="#FF9800", fg="white", command=self.clear_fields)
        self.clear_button.pack(side="left", expand=True, padx=10)
        
        self.delete_button = tk.Button(self.button_frame, text="Delete Contact", font=("Arial", 12, "bold"), bg="#F44336", fg="white", command=self.delete_contact)
        self.delete_button.pack(side="left", expand=True, padx=10)
        
        # Contacts List Frame
        self.contacts_frame = tk.Frame(root, bg="#E8EAF6", bd=5)
        self.contacts_frame.place(relx=0.5, rely=0.7, relwidth=0.9, relheight=0.25, anchor="center")
        
        self.contacts_tree = ttk.Treeview(self.contacts_frame, columns=("Name", "Phone", "Email"), show="headings")
        self.contacts_tree.heading("Name", text="Name")
        self.contacts_tree.heading("Phone", text="Phone")
        self.contacts_tree.heading("Email", text="Email")
        self.contacts_tree.pack(fill="both", expand=True)
        
        self.contacts_tree.bind("<<TreeviewSelect>>", self.populate_fields)
        
    # Resize Background Image
    def resize_background(self, event):
        new_width = event.width
        new_height = event.height
        resized_image = self.bg_image.resize((new_width, new_height), Image.ANTIALIAS)
        self.bg_photo = ImageTk.PhotoImage(resized_image)
        self.canvas.itemconfig(self.bg_image_on_canvas, image=self.bg_photo)
    
    # Add/Update Contact Method
    def add_or_update_contact(self):
        name = self.name_entry.get().strip()
        phone = self.phone_entry.get().strip()
        email = self.email_entry.get().strip()
        
        if name and phone and email:
            if name in self.contacts:
                messagebox.showinfo("Updated", f"Contact '{name}' updated successfully.")
            else:
                messagebox.showinfo("Added", f"Contact '{name}' added successfully.")
                
            self.contacts[name] = Person(name, phone, email)
            self.display_contacts()
            self.clear_fields()
        else:
            messagebox.showerror("Error", "All Fields are required!")
    
    # Delete Contact Method
    def delete_contact(self):
        selected_item = self.contacts_tree.selection()
        if selected_item:
            name = self.contacts_tree.item(selected_item, "values")[0]
            if name in self.contacts:
                del self.contacts[name]
                messagebox.showinfo("Success", f"Contact '{name}' deleted successfully.")
                self.display_contacts()
                self.clear_fields()
            else:
                messagebox.showerror("Error", "Contact Not Found!")
        else:
            messagebox.showerror("Error", "Select a Contact to Delete!")
    
    # Display all Contacts Method
    def display_contacts(self):
        for row in self.contacts_tree.get_children():
            self.contacts_tree.delete(row)
            
        for name, contact in sorted(self.contacts.items()):
            self.contacts_tree.insert("", tk.END, values=(contact.name, contact.phone, contact.email))
    
    # Populate fields when a contact is selected
    def populate_fields(self, event):
        selected_item = self.contacts_tree.selection()
        if selected_item:
            name, phone, email = self.contacts_tree.item(selected_item, "values")
            self.name_entry.delete(0, tk.END)
            self.name_entry.insert(0, name)
            self.phone_entry.delete(0, tk.END)
            self.phone_entry.insert(0, phone)
            self.email_entry.delete(0, tk.END)
            self.email_entry.insert(0, email)
            
    # Clear input fields
    def clear_fields(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        

# Main Application
if __name__ == "__main__":
    root = tk.Tk()
    app = ContactsApp(root)
    root.mainloop()