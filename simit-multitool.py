import sys
import time
import socket
import pyautogui
import requests
import webbrowser
import subprocess
import os
import colorama
from colorama import Fore, init

init(autoreset=True)





def symbol_intro():
    print(Fore.RED + "               ██████╗ ███████╗██████╗ ███████╗██╗███╗   ███╗██╗████████╗")
    print(Fore.RED + "               ██╔══██╗██╔════╝██╔══██╗██╔════╝██║████╗ ████║██║╚══██╔══╝")
    print(Fore.RED + "               ██████╔╝█████╗  ██║  ██║███████╗██║██╔████╔██║██║   ██║   ")
    print(Fore.RED + "               ██╔══██╗██╔══╝  ██║  ██║╚════██║██║██║╚██╔╝██║██║   ██║   ")
    print(Fore.RED + "               ██║  ██║███████╗██████╔╝███████║██║██║ ╚═╝ ██║██║   ██║   ")
    print(Fore.RED + "               ╚═╝  ╚═╝╚══════╝╚═════╝ ╚══════╝╚═╝╚═╝     ╚═╝╚═╝   ╚═╝   ")
    print(Fore.RED + "                               Made by @redsimit ")


symbol_intro()


def available_commands():
    print(Fore.GREEN + """
        Available commands: ═══════════════════╗═══════════════════════════════════════╗
        ╚═ Networking:                         ╚═ Attacking:                           ╚═ Other:
          ╚═ [1] Port scanner                      ╚═ [5] Spammbot                        ╚═ q = quit
             [2] Geolocator                           [6] phishing                           help
             [3] Osint tool                           [7] Webcam Hack                        support
             [4] Prank call                           [8] Payload + Listener                 [9]download my tools    
                                                      [10] Metasploit + custom exploit       [11] Join discord  
                                                      [12] RedSploit                         [99] ALHack 
        """)


available_commands()


def help():
    available_commands()


def clear_terminal():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def geolocator():
    print(Fore.RED + """
                         ▄████  ▓█████   ▒█████    ██████   ██▓  ███▄ ▄███▓  ██▓▄▄ ▄█████▓
                         ██▒ ▀█▒ ▓█   ▀  ▒██▒  ██▒ ▒██    ▒  ▓██▒ ▓██▒▀█▀ ██▒ ▓██▒▓   ██▒ ▓▒
                        ▒██░▄▄▄ ░▒███    ▒██░  ██▒ ░ ▓██▄    ▒██▒ ▓██    ▓██░ ▒██▒▒  ▓██░ ▒░
                        ░▓█  ██▓▒ ▓█  ▄  ▒██   ██░   ▒   ██▒ ░██░ ▒██    ▒██ ░ ██░░  ▓██▓ ░ 
                        ░▒▓███▀▒░ ▒████▒ ░ ████▓▒░ ▒██████▒▒ ░██░ ▒██▒   ░██▒░ ██░  ▒██▒ ░ 
                         ░▒   ▒ ░░ ▒░ ░░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░░▓  ░ ▒░   ░  ░░▓    ▒ ░░   
                          ░   ░  ░ ░  ░  ░ ▒ ▒░ ░ ░▒  ░ ░ ▒ ░░  ░      ░ ▒ ░    ░    
                         ░ ░   ░    ░   ░ ░ ░ ▒  ░  ░  ░   ▒ ░░      ░    ▒ ░  ░      
                               ░    ░  ░    ░ ░        ░   ░         ░    ░           
                                              Made by @Redsimit                                             """)
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


def port_scanner():
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


def reverse_shell():
    print(Fore.RED + "INSTALLING THE TOOL (enter to continue) ")
    time.sleep(0.5)
    repo = "https://github.com/Simit6155/SchimmelBox-Warriors.git"
    clone_cmd = ["git", "clone", repo]
    subprocess.run(clone_cmd)
    os.chdir("SchimmelBox-Warriors")
    print(Fore.RED + "YOU NEED TO HAVE THE CLIENT.PY RUNNING ON THE SYSTEM U WANNA CONNECT TO !!! (enter to continue)")
    time.sleep(3)
    subprocess.run(["python3", "server.py"])


def zphisher():
    phish_repo = "https://github.com/htr-tech/zphisher.git"
    phish_clone = ["git", "clone", phish_repo]
    subprocess.run(phish_clone)

    os.chdir("zphisher")
    mod_phish = ["chmod", "+x", "zphisher.sh"]
    subprocess.run(mod_phish)
    start_phish = ["./zphisher.sh"]
    subprocess.run(start_phish)


def cam_phish():
    cam_repo = "https://github.com/techchipnet/CamPhish.git"
    cam_clone = ["git", "clone", cam_repo]
    subprocess.run(cam_clone)

    os.chdir("CamPhish")
    mod_cam = ["chmod", "+x", "CamPhish.sh"]
    subprocess.run(mod_cam)
    start_cam = ["./CamPhish.sh"]
    subprocess.run(start_cam)


def osint_tool():
    start_sherlock = ["sherlock", "-h"]
    subprocess.run(start_sherlock)


def phone_caller():
    print(Fore.RED + """
            ▄▄▄·    ▄▄·  ▄▄▄· ▄▄▌  ▄▄▌  ▄▄▄ .▄▄▄  
            ▐█ ▄█   ▐█ ▌▪▐█ ▀█ ██•  ██•  ▀▄.▀·▀▄ █·
             ██▀·   ██ ▄▄▄█▀▀█ ██▪  ██▪  ▐▀▀▪▄▐▀▀▄ 
            ▐█▪·•   ▐███▌▐█ ▪▐▌▐█▌▐▌▐█▌▐▌▐█▄▄▌▐█•█▌
            .▀    ▀ ·▀▀▀  ▀  ▀ .▀▀▀ .▀▀▀  ▀▀▀ .▀  ▀""")
    print(Fore.RED + "~~~~ Author @Redsimit ~~~~ ")
    number = input(Fore.GREEN + "Enter number: ")
    print(Fore.GREEN + "Calling dont move your mouse . . . . ")
    webbrowser.open("https://callmyphone.org")
    time.sleep(5)
    pyautogui.leftClick(902, 389)
    time.sleep(1)
    pyautogui.typewrite(number)
    time.sleep(0.5)
    pyautogui.leftClick(1257, 389)


def update():
    if os.name == "nt":
        pass
    else:
        update = ["sudo", "apt", "update", "&&", "sudo", "apt", "upgrade", "-y"]
        subprocess.run(update)


def albanian_ht():
    aht_repo = "https://github.com/AlbanianCyberArmy/Albanian-Hacking-Tool.git"
    aht_clone = ["git", "clone", aht_repo]
    subprocess.run(aht_clone)
    os.chdir("ALHacking")
    alhack_access = ["chmod", "+x", "alhack.sh"]
    subprocess.run(alhack_access)
    alhack_start = ["bash", "alhack.sh"]
    subprocess.run(alhack_start)


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


def install_mytools():
    port_repo = "https://github.com/Simit6155/Smart-Port-scanner.git"
    port_clone = ["git", "clone", port_repo]
    subprocess.run(port_clone)

    spam_repo = "https://github.com/Simit6155/RedSpam.git"
    spam_clone = ["git", "clone", spam_repo]
    subprocess.run(spam_clone)

    redshell_repo = "https://github.com/Simit6155/SchimmelBox-Warriors.git"
    redshell_clone = ["git", "clone", redshell_repo]
    subprocess.run(redshell_clone)

    autoclicker_repo = "https://github.com/Simit6155/Auto-Clicker.git"
    autoclicker_clone = ["git", "clone", autoclicker_repo]
    subprocess.run(autoclicker_clone)

    geolocator_repo = "https://github.com/Simit6155/GeoLocator.git"
    geolocator_clone = ("git", "clone", geolocator_repo)
    subprocess.run(geolocator_clone)

    webbrowser.open("https://github.com/Simit6155")


def custom_sploit():
    print(Fore.RED + "Installing . . . ")
    metasploit_repo = "https://github.com/rapid7/metasploit-framework.git"
    metasploit_clone = ["git", "clone", metasploit_repo]
    subprocess.run(metasploit_clone)

    custom_exploit_repo = "https://github.com/FOLKS-iwd/CVE-2025-24071-msfvenom?tab=readme-ov-file"
    custom_exploit_clone = ["git", "clone", custom_exploit_repo]
    subprocess.run(custom_exploit_clone)

    run_meta = "msfconsole"
    subprocess.run(run_meta)


def outro():
    webbrowser.open("https://discord.gg/FyKAf9crA4")


def RedSploit():
    def intro():
        print(Fore.CYAN + """
                             ▄▀▀▄▀▀▀▄  ▄▀▀█▄▄▄▄  ▄▀▀█▄▄   ▄▀▀▀▀▄  ▄▀▀▄▀▀▀▄  ▄▀▀▀▀▄    ▄▀▀▀▀▄   ▄▀▀█▀▄    ▄▀▀▀█▀▀▄ 
                            █   █   █ ▐  ▄▀   ▐ █ ▄▀   █ █ █   ▐ █   █   █ █    █    █      █ █   █  █  █    █  ▐ 
                            ▐  █▀▀█▀    █▄▄▄▄▄  ▐ █    █    ▀▄   ▐  █▀▀▀▀  ▐    █    █      █ ▐   █  ▐  ▐   █     
                             ▄▀    █    █    ▌    █    █ ▀▄   █     █          █     ▀▄    ▄▀     █        █      
                            █     █    ▄▀▄▄▄▄    ▄▀▄▄▄▄▀  █▀▀▀    ▄▀         ▄▀▄▄▄▄▄▄▀ ▀▀▀▀    ▄▀▀▀▀▀▄   ▄▀       
                            ▐     ▐    █    ▐   █     ▐   ▐      █           █                █       █ █         
                                       ▐        ▐                ▐           ▐                ▐       ▐ ▐         
                                                           @Redsimit
        """)
        print(Fore.CYAN + """                   
                                               Available Reverse shell clients:
                                                 [1] Python     [3] Powershell
                                                 [2] Rust       [4] Bash 

                                               Available Reverse shell Listeners: 
                                                             Python         
             """)


    def Python():
        python_repo = "https://github.com/Simit6155/SchimmelBox-Warriors.git"
        python_clone = ["git", "clone", python_repo]
        subprocess.run(python_clone)
        print(Fore.GREEN + "You need to change the ip in the file")
        print(Fore.GREEN + "Installed successfully!")


    def Rust():
        rust_repo = "https://github.com/Simit6155/rust-client.git"
        rust_clone = ["git", "clone", rust_repo]
        subprocess.run(rust_clone)
        print(Fore.GREEN + "You need to change the ip in the file")
        print(Fore.GREEN + "Installed successfully!")


    def Powershell():
        powershell_repo = "https://github.com/Simit6155/revshell-pwrshell.git"
        powershell_clone = ["git", "clone", powershell_repo]
        subprocess.run(powershell_clone)
        print(Fore.GREEN + "You need to change the ip in the file")
        print(Fore.GREEN + "Installed successfully!")


    def Bash():
        bash_repo = "https://github.com/Simit6155/client.bat.git"
        bash_clone = ["git", "clone", bash_repo]
        subprocess.run(bash_clone)
        print(Fore.GREEN + "You need to change the ip in the file")
        print(Fore.GREEN + "Installed successfully!")


    def PythonListener():
        python_listener_repo = "https://github.com/Simit6155/python-listenerd.git"
        python_listener_clone = ["git", "clone", python_listener_repo]
        subprocess.run(python_listener_clone)
        print(Fore.GREEN + "Installed successfully!")


    try:
        intro()
        command2 = ""
        while command2 != "q":
            command2 = input(Fore.CYAN + "| > ")

            if command2 == "1":
                Python()

            elif command2 == "2":
                Rust()

            elif command2 == "3":
                Powershell()

            elif command2 == "4":
                Bash()

            elif command2 == "q":
                break

            elif command2 == "python".lower():
                PythonListener()

            else:
                print(Fore.GREEN + "[~] Unknown command.")


    except KeyboardInterrupt:
        print(Fore.RED + """
    [!] Keyboard interrupt detected. Closing in 2""")

        time.sleep(1)

        print(Fore.RED + """
    [!] Closing in 1""")

        time.sleep(0.5)

        print(Fore.RED + """
    closing program...""")


try:
    command = ""
    while command != "q":
        command = input(Fore.RED + "| > ")

        if command == "q":
            clear_terminal()
            print(Fore.GREEN + "closing program...")
            time.sleep(1)
            break


        elif command == "1":
            try:
                clear_terminal()
                update()
                clear_terminal()
                port_scanner()

            except:
                print(Fore.RED + "Error occurred. Closing")


        elif command == "2":
            try:
                clear_terminal()
                update()
                clear_terminal()
                geolocator()

            except:
                print(Fore.RED + "Error occurred. Closing")


        elif command == "3":
            try:
                clear_terminal()
                update()
                clear_terminal()
                osint_tool()

            except:
                print("""
[-] Error: Linux needed
[-] Try another command """)


        elif command == "4":
            try:
                clear_terminal()
                update()
                clear_terminal()
                phone_caller()

            except:
                print(Fore.RED + "Error occurred. Closing")


        elif command == "5":
            try:
                clear_terminal()
                update()
                clear_terminal()
                spamm_bot()

            except:
                print(Fore.RED + "Error occurred. Closing")


        elif command == "6":
            try:
                clear_terminal()
                update()
                clear_terminal()
                zphisher()

            except:
                print("""
[-] Error: Linux needed
[-] Try another command """)


        elif command == "7":
            try:
                clear_terminal()
                update()
                clear_terminal()
                cam_phish()

            except:
                print("""
[-] Error: Linux needed
[-] Try another command """)


        elif command == "8":
            try:
                clear_terminal()
                update()
                clear_terminal()
                reverse_shell()

            except:
                print("""
[-] Error: Linux needed
[-] Try another command """)


        elif command == "9":
            try:
                clear_terminal()
                update()
                clear_terminal()
                install_mytools()

            except:
                print("""
[-] Error: Linux needed
[-] Try another command """)


        elif command == "10":
            try:
                clear_terminal()
                update()
                clear_terminal()
                custom_sploit()

            except:
                print("""
[-] Error: Linux needed
[-] Try another command """)


        elif command == "11":
            try:
                outro()

            except:
                print(Fore.RED + "Error occurred. Closing")


        elif command == "12":
            try:
                clear_terminal()
                update()
                clear_terminal()
                RedSploit()

            except:
                print(Fore.RED + "Error occurred. Closing")


        elif command == "help":
            try:
                help()

            except:
                print(Fore.RED + "Error occurred. Closing")


        elif command == "support":
            try:
                support_me()

            except:
                print(Fore.RED + "Error occurred. Closing")


        elif command == "99":
            try:
                clear_terminal()
                albanian_ht()

            except:
                print("""
[-] Error: Linux needed
[-] Try another command """)


        else:
            print(Fore.RED + "[~] Unknown command... use command help to see available commands")

except KeyboardInterrupt:
    clear_terminal()

    print(Fore.RED + """
[!] Keyboard interrupt detected. Closing """)
    sys.exit()
