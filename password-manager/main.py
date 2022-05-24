import tkinter as tk
from tkinter import messagebox
from tkinter import *
import random
import json

# json.dump json.load json.update

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_list += [random.choice(letters) for _ in range(nr_letters)]

    password_list += [random.choice(symbols) for _ in range(nr_symbols)]

    password_list += [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password_list)

    passwd = "".join(password_list)
    password.insert(0, passwd)

# ---------------------------SEARCH USER AND PASSWORD------------------------#

def search():
    a = website.get()
    if len(a)==0:
        messagebox.showerror(title="Error",message="Username cannot be empty!")
        return
    try:
        with open("data.json", 'r') as record:
            data = json.load(record)
            if a in data:
                messagebox.showinfo(title=a, message=f"Email:{data[a]['email']}\nPassword:{data[a]['password']}")
            else:
                messagebox.showwarning(title="Not in the list",message="No information of website!")
    except FileNotFoundError:
        print("There is no .json file!")
        file = open("data.json", 'w')
        new_data = {
            a: {
                "email": "None",
                "password": "None"
            }
        }
        json.dump(new_data, file, indent=4)
        file.close()

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    a = website.get()
    b = user.get()
    c = password.get()
    new_data = {
        a: {
            "email":b,
            "password":c
        }
    }

    if len(a) == 0 or len(c) == 0:
        messagebox.showwarning(title="Blank input!", message="Don't leave any of the fill empty!")
        return
    else:
        try:
            with open("data.json", 'r') as record:
                # json.dump(new_data, record, indent=4)
                data = json.load(record)
                data.update(new_data)
        except FileNotFoundError:
            print("You dont have tht data.json lah dog, i open for u")
            with open("data.json", 'w') as record:
                json.dump(new_data, record, indent=4)
        else:
            with open("data.json", 'w') as record:
                json.dump(data, record, indent=4)
        finally:
            password.delete(0, len(c))
            website.delete(0, len(a))


# ---------------------------- SHOW PASSWORD ------------------------------- #
def show_password():
    if c_v1.get() == 1:
        password.config(show="")
    else:
        password.config(show="*")

# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.config(padx=20, pady=20, bg="white")
window.title("Password Manager")
canvas = tk.Canvas(height=200, width=200, highlightthickness=0, bg="white")
logo = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

label_1 = tk.Label(text="Website:", bg="white")
label_1.grid(row=1, column=0)

label_2 = tk.Label(text="Email\\Username:", bg="white")
label_2.grid(row=2, column=0)

label_3 = tk.Label(text="Password:", bg="white")
label_3.grid(row=3, column=0)

website = tk.Entry(width=50, bd=2)
website.grid(row=1, column=1, columnspan=2, sticky=tk.W)
website.focus_set()

user = tk.Entry(width=50, bd=2)
user.grid(row=2, column=1, columnspan=2, sticky=tk.W)
user.insert(0, "dota782x@gmail.com")

password = tk.Entry(bd=2, show="*")
password.grid(row=3, column=1, sticky=tk.W)

c_v1 = IntVar(value=0)
c1 = tk.Checkbutton(text='Show Password', variable=c_v1, onvalue=1, offvalue=0, command=show_password,bg="white")
c1.grid(row=3, column=2, sticky=tk.W)


generate_button = tk.Button(text="Generate Password",command=generate_password)
generate_button.grid(column=3, row=3, sticky=tk.W)

add_button = tk.Button(text="Add", width=36, command=save_password)
add_button.grid(column=1, row=4, columnspan=2, sticky=tk.W)

search_button = tk.Button(text="Search",command=search)
search_button.grid(row=1, column=3, columnspan=2)

window.mainloop()


