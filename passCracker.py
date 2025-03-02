#!/usr/bin/env python
# coding: utf-8

# In[4]:


import tkinter as tk
from tkinter import messagebox, scrolledtext
import itertools
import string
import threading



CORRECT_PASSWORD = ""

# GUI Setup
root = tk.Tk()
root.title("Password Cracker")

# Username Entry
tk.Label(root, text="Username:").grid(row=0, column=0, padx=5, pady=5)
entry_username = tk.Entry(root)
entry_username.grid(row=0, column=1, padx=5, pady=5)

# Password Entry
tk.Label(root, text="Password (5 letters only):").grid(row=1, column=0, padx=5, pady=5)
entry_password = tk.Entry(root, show="*")  # Hide password input
entry_password.grid(row=1, column=1, padx=5, pady=5)

# Start Attack Button
btn_attack = tk.Button(root, text="Start Attack", command=start_attack)
btn_attack.grid(row=2, column=0, columnspan=2, pady=10)

# Output Text Box 
text_output = scrolledtext.ScrolledText(root, width=40, height=15)
text_output.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()


def start_attack():
    global CORRECT_PASSWORD
    username = entry_username.get()
    CORRECT_PASSWORD = entry_password.get()

    if len(CORRECT_PASSWORD) != 5 or not CORRECT_PASSWORD.isalpha():
        messagebox.showerror("Error", "Password must be exactly 5 letters (A-Z, a-z)!")
        return

    text_output.delete("1.0", tk.END)  # Clear previous logs
    update_output(f"Starting attack on user: {username}\n")

    # Run attack in a separate thread so GUI doesn't freeze
    attack_thread = threading.Thread(target=lambda: (
        dictionary_attack(username) or brute_force_attack(username)
    ))
    attack_thread.start()

    
def dictionary_attack(username):
    with open('default-passwords.txt', 'r') as file:
        for line in file:
            password = line.strip()
            
            if password == CORRECT_PASSWORD:
                update_output(f"Dictionary Attack Success! Password for {username} is: {password}\n")
                messagebox.showinfo("Success", f"Password for {username} found: {password}")
                return True
            
    update_output("Dictionary Attack Failed. Starting brute force...\n")
    return False


def brute_force_attack(username):
    chars = string.ascii_letters  # a-z, A-Z
    
    for attempt in itertools.product(chars, repeat=5):  # Only 5-letter
        password = ''.join(attempt)
        update_output(f"Trying: {password}\n") 
        root.update_idletasks()  #for gui
       
        if password == CORRECT_PASSWORD:
            update_output(f"Brute Force Attack Success! Password for {username} is: {password}\n")
            messagebox.showinfo("Success", f"Password for {username} found: {password}")
            return True
    
    update_output("Brute Force Attack Failed.\n")
    messagebox.showerror("Failed", "Password could not be cracked.")
    return False





def update_output(text):
    text_output.insert(tk.END, text)
    text_output.see(tk.END)  #to auto scroll





# In[ ]:




