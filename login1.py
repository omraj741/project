import tkinter as tk
from tkinter import messagebox
import subprocess

def verify_user(username, password):
    if username == 'admin' and password == 'admin':
        messagebox.showinfo('Success', 'Logged in successfully!')
        open_student_management_system()
    else:
        messagebox.showerror('Error', 'Invalid username or password')

def login():
    username = username_entry.get()
    password = password_entry.get()
    verify_user(username, password)

def open_student_management_system():
    main.destroy()  
    subprocess.run(["python", "C:\\Users\\rajom\\OneDrive\\Desktop\\1.py"])

main = tk.Tk()
main.title('Login Page')
main.geometry('230x250')

image_path ="C:\\Users\\rajom\\Downloads\\th.png"
img = tk.PhotoImage(file=image_path)


image_label = tk.Label(main, image=img)
image_label.image = img  

image_label.grid(row=0, column=0, columnspan=2)

username_label = tk.Label(main, text='Username:')
username_label.grid(row=1, column=0)

username_entry = tk.Entry(main)
username_entry.grid(row=1, column=1)

password_label = tk.Label(main, text='Password:')
password_label.grid(row=2, column=0)

password_entry = tk.Entry(main, show='*')
password_entry.grid(row=2, column=1)

login_button = tk.Button(main, text='Login', command=login)
login_button.grid(row=3, column=0, columnspan=2)

main.mainloop()
