import tkinter as tk
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    secure_password = ''.join(random.choice(characters) for _ in range(length))
    return secure_password

def generate_button_click():
    password_length = int(length_entry.get())
    password = generate_password(password_length)
    result_label.config(text="Generated Password: " + password)

# Create the main application window
app = tk.Tk()
app.title("Password Generator")

# Create widgets
length_label = tk.Label(app, text="Password Length:")
length_label.pack()
length_entry = tk.Entry(app)
length_entry.pack()

generate_button = tk.Button(app, text="Generate Password", command=generate_button_click)
generate_button.pack()

result_label = tk.Label(app, text="")
result_label.pack()

# Start the main event loop
app.mainloop()

