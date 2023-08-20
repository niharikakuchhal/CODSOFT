# """
#     Password Generator
# """
# import random
# import string
# import pyperclip
# import os

# def generate_password(length:int,
#                       use_lower:bool=True,
#                       use_upper:bool = True,
#                       use_number : bool = True,
#                       use_specials:bool  = False
#                       ):
#     """
#         Generate a password of the specified length.
#         Args:
#             length (int): The desired number of characters in your generated password
#         Keyword Arguments:
#             use_lower {bool} -- Whether to include lowercase letters [default: True]
#             use_upper {bool} -- Whether ot not to include uppercase letters [default: True]
#             use_number {bool} -- Whether or not to include numbers[default: True]
#             use_specials{bool}--Whether or not to include special symbols[default:False].
#         Returns:
#             str -- A string containing randomly selected alphanumeric 
#             and/or special character values based on user input.
            
#     """
#     # Create an empty list for storing our final password
#     passwrd= ''
#     if use_lower:
#         passwrd+=string.ascii_lowercase
#     if use_upper:
#         passwrd += string.ascii_uppercase
#     if use_number:
#         passwrd += string.digits
#     if use_specials:
#         passwrd += string.punctuation

#     if not passwrd:
#         raise ValueError('You must select at least one type of character')
#     return ''.join((random.choice(passwrd)for _ in range(0,length)))

# def main():
#     """
#         Display the Password and save into the clipboard
#     """
#     print("Welcome to Password Locker")
#     try:
#         num_pass = int(input("\
#                              How many passwords do you want to generate? "))
#         length = int(input("\
#                       Enter the desired length of the password: "))
#         lower = input('\
#                       Do you wish to include LOWERCASE letters?(y/n)').lower()=='y'
#         upper = input('\
#                       Do you wish to include UPPERCASE letters?(y/n) ').lower()== 'y'
#         digit = input("\
#                       Do you wish to include NUMBERS ?(y/n)").lower() == "y"
#         special = input("\
#                       Do you wish to include SPECIAL SYMBOLS?(y/n)" ).lower()=="y"
#         for _ in range(num_pass):
#             password = generate_password(length ,
#                                    use_lower = lower,
#                                    use_upper = upper,
#                                    use_number = digit,
#                                    use_specials=special)
#             print("Generated Password: "+password)
#             copy_choice = input('copy this password to clipboard? (y/n)').lower()
#             if copy_choice:
#                 pyperclip.copy(password)
#                 print("Password copied to clipboard!")
#     except ValueError as error:
#         print ("Invalid Input!! Please enter alid values",error )

# if __name__ == '__main__':
#     os.system('cls')
#     main()

import random
import string
import pyperclip
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("400x450")

        # Load and display the background image
        bg_image = Image.open("password.jpg") 
        self.background_photo = ImageTk.PhotoImage(bg_image)
        self.bgLabel = tk.Label(root, image = self.background_photo)
        self.bgLabel.place(relwidth=1, relheight=1)
        # self.root.configure(bg="#f0f0f0")

        self.heading_label = tk.Label(root, text="Password Generator", font=("Helvetica", 16, "bold"), bg="#f0f0f0")
        self.heading_label.pack(pady=20)

        self.length_label = tk.Label(root, text="Password Length:", font=("Helvetica", 12), bg="#f0f0f0")
        self.length_label.pack()
        self.length_entry = tk.Entry(root, font=("Helvetica", 12))
        self.length_entry.pack()

        self.lower_var = tk.IntVar()
        self.lower_checkbox = tk.Checkbutton(root, text="Include Lowercase Letters", variable=self.lower_var, font=("Helvetica", 10), bg="#f0f0f0")
        self.lower_checkbox.pack()

        self.upper_var = tk.IntVar()
        self.upper_checkbox = tk.Checkbutton(root, text="Include Uppercase Letters", variable=self.upper_var, font=("Helvetica", 10), bg="#f0f0f0")
        self.upper_checkbox.pack()

        self.number_var = tk.IntVar()
        self.number_checkbox = tk.Checkbutton(root, text="Include Numbers", variable=self.number_var, font=("Helvetica", 10), bg="#f0f0f0")
        self.number_checkbox.pack()

        self.special_var = tk.IntVar()
        self.special_checkbox = tk.Checkbutton(root, text="Include Special Symbols", variable=self.special_var, font=("Helvetica", 10), bg="#f0f0f0")
        self.special_checkbox.pack()

        self.generate_button = tk.Button(root, text="Generate Password", command=self.generate_password, font=("Helvetica", 12), bg="#4CAF50", fg="white", padx=10, pady=5)
        self.generate_button.pack(pady=20)

    def generate_password(self):
        length = int(self.length_entry.get())
        use_lower = bool(self.lower_var.get())
        use_upper = bool(self.upper_var.get())
        use_number = bool(self.number_var.get())
        use_specials = bool(self.special_var.get())

        if length < 4:
            length = 4  # Ensure a minimum length of 4

        try:
            password = self._generate_password(length, use_lower, use_upper, use_number, use_specials)
            pyperclip.copy(password)
            messagebox.showinfo("Generated Password", f"Password generated and copied to clipboard:\n{password}")
        except ValueError as error:
            messagebox.showerror("Error", f"Invalid input: {error}")

    def _generate_password(self, length, use_lower, use_upper, use_number, use_specials):
        passwrd = ''
        if use_lower:
            passwrd += string.ascii_lowercase
        if use_upper:
            passwrd += string.ascii_uppercase
        if use_number:
            passwrd += string.digits
        if use_specials:
            passwrd += string.punctuation

        if not passwrd:
            raise ValueError('You must select at least one type of character')

        return ''.join((random.choice(passwrd) for _ in range(length)))

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
