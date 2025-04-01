import random
import string
import tkinter as tk
from tkinter import ttk, messagebox

def generate_username():
    adjectives = ["Cool", "Soft", "Genius", "Bright", "Brilliant", "Silent", "Brave", "Intelligent"]
    nouns = ["Tiger", "Nehuu", "Smith", "Storm", "John", "Rashi", "Eagle", "Butterfly"]
    
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    
    extra_part = ""
    if extra_var.get():
        choice_type = choice_var.get()
        if choice_type == "num":
            extra_part = str(random.randint(100, 999))
        elif choice_type == "char":
            extra_part = random.choice(string.punctuation)
        elif choice_type == "both":
            extra_part = str(random.randint(100, 999)) + random.choice(string.punctuation)
    
    username = adjective + noun + extra_part
    username_label.config(text=f"Generated Username: {username}")
    
    with open("usernames.txt", "a") as file:
        file.write(username + "\n")
    
    messagebox.showinfo("Success", "Username saved to usernames.txt!")

def close_app():
    root.destroy()

root = tk.Tk()
root.title("Username Generator")
root.geometry("900x550")
root.configure(bg="#FED168")

style = ttk.Style()
style.configure("TButton", font=("Times New Roman", 20, "bold"), padding=10, relief="flat", width=20)
style.configure("TLabel", font=("Times New Roman", 18, "bold"), foreground="black", background="#FED168")
style.configure("TCheckbutton", font=("Times New Roman", 18), background="#FED168")
style.configure("TRadiobutton", font=("Times New Roman", 18), background="#FED168")

header = tk.Label(root, text="✨ Username Generator ✨", font=("Times New Roman", 24, "bold"), fg="black", bg="#FED168")
header.pack(pady=10)

extra_var = tk.BooleanVar()
extra_check = ttk.Checkbutton(root, text="Add numbers or special characters", variable=extra_var)
extra_check.pack(pady=5)

choice_var = tk.StringVar(value="num")
radiobutton1 = ttk.Radiobutton(root, text="Numbers", variable=choice_var, value="num")
radiobutton2 = ttk.Radiobutton(root, text="Special Characters", variable=choice_var, value="char")
radiobutton3 = ttk.Radiobutton(root, text="Both", variable=choice_var, value="both")

radiobutton1.pack()
radiobutton2.pack()
radiobutton3.pack()

generate_btn = tk.Button(root, text="Generate Username", command=generate_username, font=("Times New Roman", 18, "bold"), bg="green", fg="black", padx=10, pady=5)
generate_btn.pack(pady=15)

exit_btn = tk.Button(root, text="Exit", command=close_app, font=("Times New Roman", 18, "bold"), bg="red", fg="black", padx=10, pady=5)
exit_btn.pack(pady=5)

username_label = ttk.Label(root, text="", font=("Times New Roman", 18), foreground="black", background="#FED168")
username_label.pack(pady=15)

root.mainloop()
