import tkinter as tk
from tkinter import messagebox
import secrets # Generate cryptographically strong pseudo-random numbers suitable for managing 
# secrets such as account authentication, tokens, and similar.

import string # module consists of different string constants
class password_generator:
    def __init__(self, root) -> None:
        self.root = root
        self.root.title("ADVANCED PASSWORD GENERATOR")
        
        tk.Label(root, text = "Password Length: ").grid(row = 0, column= 0, padx= 10, pady= 10)
        self.length_var = tk.IntVar(value= 12)
        tk.Entry(root, textvariable= self.length_var).grid(row = 0, column = 1, padx= 10, pady= 10)
        
        self.include_upper = tk.BooleanVar(value = True)
        self.include_digits = tk.BooleanVar(value = True)
        self.include_special = tk.BooleanVar(value = True)
        
        tk.Checkbutton(root, text = "Include UpperCase Letters", variable=self.include_upper).grid(row=1, column=0, columnspan=2, padx=10, pady=5, sticky="w")
        tk.Checkbutton(root, text = "Include Digits", variable=self.include_digits).grid(row=2, column=0, columnspan=2, padx=10, pady=5, sticky="w")
        tk.Checkbutton(root, text = "Include Special Characters", variable=self.include_special).grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky="w")
        
        tk.Button(root, text = "Generate PassWord", command=self.gen_pass).grid(row=4, column=0, padx=10, pady=10)
        tk.Button(root, text = "Copy To Clipboard", command=self.copyToClipBrd).grid(row=4, column=1, padx=10, pady=10)
        
        self.pass_var = tk.StringVar()
        tk.Entry(root, textvariable=self.pass_var, width=50).grid(row=5, column=0, columnspan=2, padx= 10, pady=10)
        
    def gen_pass(self):
        length = self.length_var.get()
        if length < 8:
            messagebox.showerror("Error", "Password length should be atleast 8 Characters.")
            return
        
        lower = string.ascii_lowercase
        upper = string.ascii_uppercase if self.include_upper.get() else ""
        digits = string.digits if self.include_digits.get() else ""
        special = string.punctuation if self.include_special.get() else ""
        
        all_char = lower + upper + digits + special
        if not all_char:
            messagebox.showerror("Error", "Atleast one character set must be selected.")
            return
        password = [secrets.choice(lower)]
        if self.include_upper.get():
            password.append(secrets.choice(upper))
        if self.include_digits.get():
            password.append(secrets.choice(digits))
        if self.include_special.get():
            password.append(secrets.choice(special)) 
            
        password += [secrets.choice(all_char) for _ in range(length - len(password))]
        secrets.SystemRandom().shuffle(password)
        self.pass_var.set(''.join(password))
    
    def copyToClipBrd(self): 
        self.root.clipboard_clear()
        self.root.clipboard_append(self.pass_var.get())
        messagebox.showinfo("Info", "Password copied to clipboard!")
        
if __name__ == "__main__":
    root = tk.Tk()
    app = password_generator(root)
    root.mainloop()