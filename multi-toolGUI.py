from tkinter import *
import pyautogui
import socket
import time
import requests
import webbrowser
from colorama import Fore,init
init(autoreset=True)





def geolocator_click():
    ip = input(Fore.GREEN + "Enter IP Address: ")
    url = f"https://ipapi.co/{ip}/json/"
    response = requests.get(url, timeout=5)
    data = response.json()

    network = data.get("network", "Unknown")
    version = data.get("version", "Unknown")
    city = data.get("city", "Unknown")
    country = data.get("country", "Unknown")
    country_name = data.get("country_name", "Unknown")
    country_code = data.get("country_code", "Unknown")
    postal = data.get("postal", "Unknown")
    timezone = data.get("timezone", "Unknown")
    asn = data.get("asn", "Unknown")
    languages = data.get("languages", "Unknown")
    country_capital = data.get("country_capital", "Unknown")
    country_area = data.get("country_area", "Unknown")

    longitude = data.get("longitude", "Unknown")
    latitude = data.get("latitude", "Unknown")

    print(Fore.GREEN + "Network: " + network)
    print(Fore.GREEN + "Version: " + version)
    print(Fore.GREEN + "City: " + city)
    print(Fore.GREEN + "Country: " + country)
    print(Fore.GREEN + "Country_name: " + country_name)
    print(Fore.GREEN + "Country_code: " + country_code)
    print(Fore.GREEN + "Country_capital: " + country_capital)
    print(Fore.GREEN + "Postal Code: " + postal)
    print(Fore.GREEN + "Timezone: " + timezone)
    print(Fore.GREEN + "ASN: " + asn)
    print(Fore.GREEN + "Languages: " + languages)
    print(Fore.GREEN + "Country_area: " + str(country_area))
    print(Fore.GREEN + "Longitude: " + str(longitude))
    print(Fore.GREEN + "Latitude: " + str(latitude))
    print(Fore.GREEN + f"https://www.google.com/maps?q={latitude},{longitude}")


def portscanner():
    choice = input(Fore.RED + """ 
    [1] Single Port scanner
    [2] Multi Port scanner

    | > """)

    if choice == "1":
        print(Fore.BLUE + """
       ▄████████  ▄█  ███▄▄▄▄      ▄██████▄   ▄█          ▄████████    ▄███████▄  ▄██████▄     ▄████████     ███        ▄████████    ▄████████ 
      ███    ███ ███  ███▀▀▀██▄   ███    ███ ███         ███    ███   ███    ███ ███    ███   ███    ███ ▀█████████▄   ███    ███   ███    ███ 
      ███    █▀  ███▌ ███   ███   ███    █▀  ███         ███    █▀    ███    ███ ███    ███   ███    ███    ▀███▀▀██   ███    █▀    ███    ███ 
      ███        ███▌ ███   ███  ▄███        ███        ▄███▄▄▄       ███    ███ ███    ███  ▄███▄▄▄▄██▀     ███   ▀  ▄███▄▄▄      ▄███▄▄▄▄██▀ 
    ▀███████████ ███▌ ███   ███ ▀▀███ ████▄  ███       ▀▀███▀▀▀     ▀█████████▀  ███    ███ ▀▀███▀▀▀▀▀       ███     ▀▀███▀▀▀     ▀▀███▀▀▀▀▀   
             ███ ███  ███   ███   ███    ███ ███         ███    █▄    ███        ███    ███ ▀███████████     ███       ███    █▄  ▀███████████ 
       ▄█    ███ ███  ███   ███   ███    ███ ███▌    ▄   ███    ███   ███        ███    ███   ███    ███     ███       ███    ███   ███    ███ 
     ▄████████▀  █▀    ▀█   █▀    ████████▀  █████▄▄██   ██████████  ▄████▀       ▀██████▀    ███    ███    ▄████▀     ██████████   ███    ███ 
                                             ▀                                                ███    ███                            ███    ███         
                """)
        print(Fore.LIGHTBLUE_EX + "THIS PORT TESTER WAS MADE BY @REDSIMIT")
        ip = input(Fore.GREEN + "IP to scan: ")
        port = int(input(Fore.GREEN + "Input the following port: "))
        time.sleep(1)
        print(Fore.LIGHTGREEN_EX + "Connecting...")
        time.sleep(2)

        try:
            socket.create_connection((ip, port), timeout=3)
            print(Fore.GREEN + "port is open")

        except socket.error:
            print(Fore.GREEN + "port is closed")


    elif choice == "2":
        print(Fore.GREEN + """
     ▄▄       ▄▄  ▄         ▄  ▄       ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄  ▄  ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄ 
    ▐░░▌     ▐░░▌▐░▌       ▐░▌▐░▌     ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌▐░▌▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
    ▐░▌░▌   ▐░▐░▌▐░▌       ▐░▌▐░▌      ▀▀▀▀█░█▀▀▀▀  ▀▀▀▀█░█▀▀▀▀  ▐░▐░▌░▌ ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌ ▀▀▀▀█░█▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌
    ▐░▌▐░▌ ▐░▌▐░▌▐░▌       ▐░▌▐░▌          ▐░▌          ▐░▌       ▐░ ░▌  ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌     ▐░▌     ▐░▌          ▐░▌       ▐░▌
    ▐░▌ ▐░▐░▌ ▐░▌▐░▌       ▐░▌▐░▌          ▐░▌          ▐░▌      ▄▄█░█▄▄ ▐░█▄▄▄▄▄▄▄█░▌▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄█░▌     ▐░▌     ▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌
    ▐░▌  ▐░▌  ▐░▌▐░▌       ▐░▌▐░▌          ▐░▌          ▐░▌     ▐░░░░░░░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌     ▐░▌     ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
    ▐░▌   ▀   ▐░▌▐░▌       ▐░▌▐░▌          ▐░▌          ▐░▌      ▀▀█░█▀▀ ▐░█▀▀▀▀▀▀▀▀▀ ▐░▌       ▐░▌▐░█▀▀▀▀█░█▀▀      ▐░▌     ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀█░█▀▀ 
    ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌          ▐░▌          ▐░▌       ▐░ ░▌  ▐░▌          ▐░▌       ▐░▌▐░▌     ▐░▌       ▐░▌     ▐░▌          ▐░▌     ▐░▌  
    ▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░▌      ▄▄▄▄█░█▄▄▄▄  ▐░▐░▌░▌ ▐░▌          ▐░█▄▄▄▄▄▄▄█░▌▐░▌      ▐░▌      ▐░▌     ▐░█▄▄▄▄▄▄▄▄▄ ▐░▌      ▐░▌ 
    ▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌     ▐░░░░░░░░░░░▌▐░▌▐░▌▐░▌▐░▌          ▐░░░░░░░░░░░▌▐░▌       ▐░▌     ▐░▌     ▐░░░░░░░░░░░▌▐░▌       ▐░▌
     ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀       ▀▀▀▀▀▀▀▀▀▀▀  ▀  ▀  ▀  ▀            ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀       ▀       ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀ 
                """)
        print(Fore.LIGHTGREEN_EX + "This Multi-Port scanner was made by @Redsimit ")
        ip = input(Fore.GREEN + "Enter IP to scan: ")
        ports = [4444, 445, 443, 8080, 20, 21, 22, 23, 25, 53, 68, 80, 110, 123, 135, 67, 137, 138, 139, 143, 161, 162,
                 389, 443, 445, 465, 514, 587, 636, 993, 995, 1080, 1433, 1521, 1723, 2049, 2121, 3306, 3389, 5432,
                 5900, 6000, 8080, 8443, 8888, 10000, 20000, 32768, 49152, 65535]

        for port in ports:
            try:
                socket.create_connection((ip, port), timeout=1)
                print(Fore.RED + f"Port {port} open ")

            except socket.error:
                print(Fore.LIGHTBLACK_EX + f"Port {port} closed ")


def spamm_bot():
    print(Fore.YELLOW + """
                        ▄▀▀█▄▄   ▄▀▀█▄▄▄▄  ▄▀▀▀▀▄  ▄▀▀▀█▀▀▄  ▄▀▀▄▀▀▀▄  ▄▀▀▀▀▄   ▄▀▀▄ ▀▀▄  ▄▀▀█▄▄▄▄  ▄▀▀▄▀▀▀▄ 
                        █ ▄▀   █ ▐  ▄▀   ▐ █ █   ▐ █    █  ▐ █   █   █ █      █ █   ▀▄ ▄▀ ▐  ▄▀   ▐ █   █   █ 
                       ▐ █    █   █▄▄▄▄▄     ▀▄   ▐   █     ▐  █▀▀█▀  █      █ ▐     █     █▄▄▄▄▄  ▐  █▀▀█▀  
                         █    █   █    ▌  ▀▄   █     █       ▄▀    █  ▀▄    ▄▀       █     █    ▌   ▄▀    █  
                       ▄▀▄▄▄▄▀  ▄▀▄▄▄▄    █▀▀▀    ▄▀       █     █     ▀▀▀▀       ▄▀     ▄▀▄▄▄▄   █     █   
                       █     ▐   █    ▐    ▐      █         ▐     ▐                █      █    ▐   ▐     ▐   
                        ▐         ▐                ▐                                ▐      ▐                  """)
    print(Fore.GREEN + "             Author: @Redsimit")
    limit = input(Fore.RED + "Input the number of messages to send: ")
    speed = input(Fore.RED + "Input the waiting time between messages: ")
    word = input(Fore.RED + "Input your message: ")
    print(Fore.GREEN + "Put your mouse on the place to spamm the messages!")
    time.sleep(3)
    print("SENDING MESSAGES... ")

    a = 1
    while a <= int(limit):
        pyautogui.typewrite(word)
        pyautogui.press("enter")
        a = a + 1
        time.sleep(float(speed))


def support_me():
    print(Fore.BLUE + """
                                     ▄▄▄▄▄▄▄▄▄▄▄  ▄         ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄        ▄  ▄    ▄  ▄▄▄▄▄▄▄▄▄▄▄ 
                                    ▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░▌      ▐░▌▐░▌  ▐░▌▐░░░░░░░░░░░▌
                                     ▀▀▀▀█░█▀▀▀▀ ▐░▌       ▐░▌▐░█▀▀▀▀▀▀▀█░▌▐░▌░▌     ▐░▌▐░▌ ▐░▌ ▐░█▀▀▀▀▀▀▀▀▀ 
                                         ▐░▌     ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌▐░▌    ▐░▌▐░▌▐░▌  ▐░▌          
                                         ▐░▌     ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░▌ ▐░▌   ▐░▌▐░▌░▌   ▐░█▄▄▄▄▄▄▄▄▄ 
                                         ▐░▌     ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌  ▐░▌  ▐░▌▐░░▌    ▐░░░░░░░░░░░▌
                                         ▐░▌     ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░▌   ▐░▌ ▐░▌▐░▌░▌    ▀▀▀▀▀▀▀▀▀█░▌
                                         ▐░▌     ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌    ▐░▌▐░▌▐░▌▐░▌            ▐░▌
                                         ▐░▌     ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌     ▐░▐░▌▐░▌ ▐░▌  ▄▄▄▄▄▄▄▄▄█░▌
                                         ▐░▌     ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌      ▐░░▌▐░▌  ▐░▌▐░░░░░░░░░░░▌
                                          ▀       ▀         ▀  ▀         ▀  ▀        ▀▀  ▀    ▀  ▀▀▀▀▀▀▀▀▀▀▀ 
    """)

    webbrowser.open("https://www.instagram.com/Redsimit")
    webbrowser.open("https://discord.gg/FyKAf9crA4")
    webbrowser.open("https://github.com/Simit6155")
    webbrowser.open("https://github.com/Simit6155?tab=repositories")




window = Tk() # makes the window
window.geometry("400x400")
window.title("RedSimit Multi-Tool")

icon = PhotoImage(file = "redsimit.png")
window.iconphoto(True,icon)
window.config(background="#171717")

label = Label(window,
              text="RS Multi-Tool",
              font=("Arial",15,"bold"),
              fg="#00FF00",
              bg="black")

label.place(x=130,y=6)

geolocator_button = Button(window,
                           text="Geo Locator",
                           command=geolocator_click,
                           font=("Comic Sans",10),
                           fg="#00FF00",
                           bg="black"
                          )
geolocator_button.place(x=120,y=80)

portscanner_button = Button(window,
                            text="Port Scanner",
                            command=portscanner,
                            font=("Comic Sans",10),
                            fg="#00FF00",
                            bg="black"
                           )
portscanner_button.place(x=115,y=140)

spammbot_button = Button(window,
                         text="Spambot",
                         command=spamm_bot,
                         font=("Comic Sans",10),
                         fg="#00FF00",
                         bg="black"
                        )
spammbot_button.place(x=220,y=80)

support_button = Button(window,
                        text="Support me",
                        command=support_me,
                        font=("Comic Sans",10),
                        fg="#00FF00",
                        bg="black"
                       )
support_button.place(x=220,y=140)


window.mainloop() # places the window
