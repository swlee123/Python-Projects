import requests
import pandas as pd
import tkinter as tk
from PIL import Image
from PIL import ImageTk
import wget
import os


LIGHT_RED = "#FF5F5D"
LIGHT_GREY = "#747E7E"
DEFAULT_FONT = ("Times",10,"bold")


response = requests.get("https://api.opendota.com/api/distributions")
country_mmr_data = response.json()["country_mmr"]["rows"]
df = pd.DataFrame(country_mmr_data)
df.to_csv("country_mmr_distribution.csv", index=False)


#------------------------- function -------------------------

def destroy_main_menu():
    by_country_button.grid_remove()
    player_info_button.grid_remove()
    hero_info_button.grid_remove()
    queries_label.grid_remove()

# grid_forget() delete them together with setting, grid_remove() can simply use grid() to recover as it remember
# those setting

def rebuild_main_menu():
    by_country_button.grid()
    player_info_button.grid()
    hero_info_button.grid()
    queries_label.grid()

def player_stat_interface():
    destroy_main_menu()
    id_label.grid(column=1, row=2, padx=18, pady=5)
    id_entry.focus()
    id_entry.grid(column=2, row=2, sticky="W", padx=18, pady=5)
    id_button.grid(column=2, row=3, sticky="W", padx=18, pady=5)

def destroy_player_interface():
    id_label.grid_remove()
    id_button.grid_remove()
    id_entry.grid_remove()

def id_comfirm():
    destroy_player_interface()
    player_id = int(id_entry.get())
    display_profile(player_id)


def display_profile(player_id):
    global image
    ## fundamental info
    player = requests.get(f"https://api.opendota.com/api/players/{player_id}")
    profile = player.json()["profile"]
    url = profile["avatar"]
    wget.download(url, "player_img.jpg")

    image = Image.open("player_img.jpg")
    image = image.resize((100, 100))
    image = ImageTk.PhotoImage(image)


    id = profile["account_id"]
    name = profile["personaname"]
    last = profile["last_login"]

    # win/loss
    win_lose = requests.get(f"https://api.opendota.com/api/players/{player_id}/wl")
    win_lose = win_lose.json()
    win_count = win_lose["win"]
    lose_count = win_lose["lose"]
    win_rate = (win_count/(win_count+lose_count))*100
    win_rate = format(win_rate,'.2f')
    # decimal reduce to 2 with this

    id_label.config(text=f"{id}\n{name}\n{last}\n{win_count}\n{lose_count}\n{win_rate}%")
    # image object cannot be local as it will be destroyed and not showed
    # display data
    picture.config(image=image)
    picture.grid(column=1, row=2, sticky="W", padx=18, pady=5)
    info_label.grid(column=1,row=2, padx=18, pady=5,sticky="E")
    id_label.grid(column=2,row=2, padx=18, pady=5,sticky="W")



#---------------- ui -------------
window = tk.Tk()
bg = Image.open("bg_img.jpg")
# bg = bg.resize((313, 176))
bg = ImageTk.PhotoImage(bg)
window.geometry("650x500")
window.title("              Dota2 Stats")
window.config(bg=LIGHT_RED)


## main menu bg
canvas1 = tk.Canvas(width=620, height=370,bg=LIGHT_RED,highlightthickness=0)
canvas1.create_image(325, 200, image=bg)
canvas1.grid(column=1, row=1,columnspan=2)

## player/heroes info
picture = tk.Label(width=100,height=100)
image = ""
info_label = tk.Label(text="Steam ID  : "
                           "\nName     : "
                           "\nLast Login: "
                           "\nWin :"
                           "\nLose:"
                           "\nWin rate  :"
                            , font=DEFAULT_FONT, bg=LIGHT_RED)
id_label = tk.Label(font=DEFAULT_FONT,bg=LIGHT_RED)




## main menu
queries_label = tk.Label(text="Please select your action",bg=LIGHT_RED)
queries_label.grid(column=1,row=2,sticky="W",padx=18,pady=5)

by_country_button = tk.Button(text="Compare by Country")
by_country_button.grid(column=1,row=3,sticky="W",padx=18,pady=5)

player_info_button = tk.Button(text="Search Steam ID", command=player_stat_interface)
player_info_button.grid(column=1,row=4,sticky="W",padx=18,pady=5)

hero_info_button = tk.Button(text="Hero Info")
hero_info_button.grid(column=1,row=5,sticky="W",padx=18,pady=5)

# player info interface
id_label = tk.Label(text="Steam32 ID :",font=DEFAULT_FONT,bg=LIGHT_RED)

id_entry = tk.Entry(text="ID HERE",width=50)

id_button = tk.Button(text="Confirm",font=DEFAULT_FONT,command=id_comfirm)






window.mainloop()



