import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class ContactsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contacts App")
        self.root.geometry("800x600")
        self.root.minsize(800, 600) #Minimum size to avoid layout breakage
        
        # Load and set the backgroud image
        self.background_image = Image.open("C:/Users/my/OneDrive/University Data/Year 2/Algorithms & Data Structures/Contacts-App/Contacts-App/background.jpg")
        
        self.background_photo = ImageTk.PhotoImage(self.background_image)
        self.bg_label = tk.Label(root, image=self.background_photo)
        self.bg_label.place(relwidth=1, relheight=1)
        
        #Contacts Dictionary
        self.contacts = {}
        
        #Title Label
        self.title_label = tk.Label(root, text="Contacts App", font=("Arial", 24, "bold"), fg="black")
        self.title_label.place(relx=0.5, rely=0.05, anchor="center")
        
        #Input Frame
        self.input_frame = tk.Frame(root, bg="#06BDFF", bd=5)
        self.input_frame.place(relx=0.5, rely= 0.2, relwidth=0.9, relheight=0.2, anchor="center")
        
        tk.Label(self.input_frame, text="Name:", font=("Arial", 14), bg="#06BDFF").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.name_entry = tk.Entry(self.input_frame, font=("Arial", 14))
        self.name_entry.grid(row=0, column=1, padx=10, pady=5, sticky="we")
        
        tk.Label(self.input_frame, text="Phone:", font=("Arial", 14), bg="#06BDFF").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.phone_entry = tk.Entry(self.input_frame, font=("Arial", 14))
        self.phone_entry.grid(row=1, column=1, padx=10, pady=5, sticky="we")
        
        #Adjust Column and Row Weight for Resizing
        self.input_frame.columnconfigure(1, weight=1)
        
        #Button Frame
        self.button_frame = tk.Frame(root, bg="#06BDFF", bd=5)
        self.button_frame.place(relx=0.5, rely=0.45, relwidth=0.9, relheight=0.1, anchor="center")
        
        self.add_button = tk.Button(self.button_frame, text="Add Contact", font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", command=self.add_contact)
        self.add_button.pack(side="left", expand=True, padx=10)
        
        self.search_button = tk.Button(self.button_frame, text="Search Contact", font=("Arial", 12, "bold"), bg="#FF9800", fg="white", command=self.search_contact)
        self.search_button.pack(side="left", expand=True, padx=10)
        
        self.delete_button = tk.Button(self.button_frame, text="Delete Contact", font=("Arial", 12, "bold"), bg="#F44336", fg="white", command=self.delete_contact)
        self.delete_button.pack(side="left", expand=True, padx=10)
        
        #Contacts List Frame
        self.contacts_frame = tk.Frame(root, bg="#E8EAF6", bd=5)
        self.contacts_frame.place(relx=0.5, rely=0.75, relwidth=0.9, relheight=0.3, anchor="center")
        
        self.contacts_list = tk.Text(self.contacts_frame, font=("Courier", 12), bg="#F5F5F5", fg="#333")
        self.contacts_list.pack(fill="both", expand=True)
        
    #Add Contact Method
    def add_contact(self):
        name = self.name_entry.get().strip()
        phone = self.phone_entry.get().strip()
        if name and phone:
            if name in self.contacts:
                messagebox.showerror("Error", "Contact Already Exists!")
            else:
                self.contacts[name] = phone
                messagebox.showinfo("Success", f"Contact '{name}' added successfully.")
                self.display_contacts()
        else:
            messagebox.showerror("Error", "Both Fields are required!")
            
    #Search Contact Method
    def search_contact(self):
        name = self.name_entry.get().strip()
        if name:
            phone = self.contacts.get(name)
            if phone:
                messagebox.showinfo("Contact Found", f"{name}: {phone}")
            else:
                messagebox.showerror("Error", "Contact Not Found!")
        else:
            messagebox.showerror("Error", "Enter a Name to Search!")
    
    #Delete Contact Method
    def delete_contact(self):
        name = self.name_entry.get().strip()
        if name:
            if name in self.contacts:
                del self.contacts[name]
                messagebox.showinfo("Success", f"Contact '{name}' deleted successfully.")
                self.display_contacts()
            else:
                messagebox.showerror("Error", "Contact Not Found!")
        else:
            messagebox.showerror("Error", "Enter a Name to Delete!")
    
    #Display all Contacts Method
    def display_contacts(self):
        self.contacts_list.delete("1.0", tk.END)
        for name, phone in sorted(self.contacts.items()):
            self.contacts_list.insert(tk.END, f"{name}: {phone}\n")
            
#Main Application
if __name__ == "__main__":
    root = tk.Tk()
    app = ContactsApp(root)
    root.mainloop()