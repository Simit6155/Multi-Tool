#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ // IMPORTS // ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import time                                                                                                          #||
import socket                                                                                                        #||
import pyautogui                                                                                                     #||
import requests                                                                                                      #||
import webbrowser                                                                                                    #||
import colorama                                                                                                      #||
from colorama import Fore, init                                                                                      #||
import subprocess                                                                                                    #||
import os                                                                                                            #||
                                                                                                                     #||
init(autoreset=True)                                                                                                 #||
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ // INTRO // ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

command = ""
while command != "q":
    def redsimit():
        print(Fore.RED + "           ██████╗ ███████╗██████╗ ███████╗██╗███╗   ███╗██╗████████╗")
        print(Fore.RED + "           ██╔══██╗██╔════╝██╔══██╗██╔════╝██║████╗ ████║██║╚══██╔══╝")
        print(Fore.RED + "           ██████╔╝█████╗  ██║  ██║███████╗██║██╔████╔██║██║   ██║   ")
        print(Fore.RED + "           ██╔══██╗██╔══╝  ██║  ██║╚════██║██║██║╚██╔╝██║██║   ██║   ")
        print(Fore.RED + "           ██║  ██║███████╗██████╔╝███████║██║██║ ╚═╝ ██║██║   ██║   ")
        print(Fore.RED + "           ╚═╝  ╚═╝╚══════╝╚═════╝ ╚══════╝╚═╝╚═╝     ╚═╝╚═╝   ╚═╝   ")
        print(Fore.RED + "                               Made by @redsimit ")

    redsimit()

    question = input(Fore.GREEN + """
Avaible commands:
q = quit

~~~~~~~~ Networking ~~~~~~~~~~~~~                                        
geo = opens geolocator                                              ~~~~~~~~~~ Attacking ~~~~~~~~~~~           
m port = opens a multi port scanner                                       spam = opens spambot    
s port = opens a single port scanner                                      rat = opens a reverse shell // linux only
osint = opens a tool for osint --- linux only                             fish = opens a phishing tool // linux only
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~                                         cam = opens a cam hacking tool // linux only
~~~~~~~~~ Other popular Multi-Tools ~~~~~~~~~                       ~~~~~~~~~~~ Support me ~~~~~~~~~~~~~~
alhack = opens albanian hacking tool --- linux only :(                  support = opens my social media accounts
///////////////////////////////////////

enter command: """)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ // MAIN // ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    if question == "geo":
        ip = input(Fore.GREEN + "Enter IP Address: ")
        print(Fore.RED + "GEOLOCATER MADE BY @REDSIMIT")
        url = f"https://ipapi.co/{ip}/json/"
        response = requests.get(url , timeout = 5)
        data = response.json()

        network = data.get("network" , "Unknown")
        version = data.get("version" , "Unknown")
        city = data.get("city" , "Unknown")
        country = data.get("country" , "Unknown")
        country_name = data.get("country_name" , "Unknown")
        country_code = data.get("country_code" , "Unknown")
        postal = data.get("postal" , "Unknown")
        timezone = data.get("timezone" , "Unknown")
        asn = data.get("asn" , "Unknown")
        languages = data.get("languages" , "Unknown")
        country_capital = data.get("country_capital" , "Unknown")
        country_area = data.get("country_area" , "Unknown")

        longitude = data.get("longitude" , "Unknown")
        latitude = data.get("latitude" , "Unknown")

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


    elif question == "q":
        print(Fore.GREEN + "closing program...")
        time.sleep(1)
        break

    elif question == "s port":
        print(Fore.RED + "THIS PORT TESTER WAS MADE BY @REDSIMIT")
        ip = "127.0.0.1"
        port = int(input(Fore.GREEN + "Input the following port: "))
        time.sleep(1)
        print(Fore.LIGHTGREEN_EX + "Connecting...")
        time.sleep(2)

        try:
            socket.create_connection((ip, port), timeout=4)
            print(Fore.GREEN + "port is open")
        except socket.error:
            print(Fore.GREEN + "port is closed")

    elif question == "m port":
        import socket
        import colorama
        from colorama import Fore, init

        init(autoreset=True)

        print(Fore.RED + "This Multi-Port tester was made by @Redsimit ")
        ip = "127.0.0.1"
        ports = [4444, 22, 8080, 443, 21, 22, 23, 25, 53, 80, 31337]

        try:
            socket.create_connection((ip, ports[0]), timeout=3)
            print(Fore.GREEN + f"Port {ports[0]} open ")
        except socket.error:
            print(Fore.GREEN + f"Port {ports[0]} closed ")

        try:
            socket.create_connection((ip, ports[1]), timeout=3)
            print(Fore.GREEN + f"Port {ports[1]} open ")
        except socket.error:
            print(Fore.GREEN + f"Port {ports[1]} closed ")

        try:
            socket.create_connection((ip, ports[2]), timeout=3)
            print(Fore.GREEN + f"Port {ports[2]} open ")
        except socket.error:
            print(Fore.GREEN + f"Port {ports[2]} closed ")

        try:
            socket.create_connection((ip, ports[3]), timeout=3)
            print(Fore.GREEN + f"Port {ports[3]} open ")
        except socket.error:
            print(Fore.GREEN + f"Port {ports[3]} closed ")

        try:
            socket.create_connection((ip, ports[4]), timeout=3)
            print(Fore.GREEN + f"Port {ports[4]} open ")
        except socket.error:
            print(Fore.GREEN + f"Port {ports[4]} closed ")

        try:
            socket.create_connection((ip, ports[5]), timeout=3)
            print(Fore.GREEN + f"Port {ports[5]} open ")
        except socket.error:
            print(Fore.GREEN + f"Port {ports[5]} closed ")

        try:
            socket.create_connection((ip, ports[6]), timeout=3)
            print(Fore.GREEN + f"Port {ports[6]} open ")
        except socket.error:
            print(Fore.GREEN + f"Port {ports[6]} closed ")

        try:
            socket.create_connection((ip, ports[7]), timeout=3)
            print(Fore.GREEN + f"Port {ports[7]} open ")
        except socket.error:
            print(Fore.GREEN + f"Port {ports[7]} closed ")

        try:
            socket.create_connection((ip, ports[8]), timeout=3)
            print(Fore.GREEN + f"Port {ports[8]} open ")
        except socket.error:
            print(Fore.GREEN + f"Port {ports[8]} closed ")

        try:
            socket.create_connection((ip, ports[9]), timeout=3)
            print(Fore.GREEN + f"Port {ports[9]} open ")
        except socket.error:
            print(Fore.GREEN + f"Port {ports[9]} closed ")

        try:
            socket.create_connection((ip, ports[10]), timeout=3)
            print(Fore.GREEN + f"Port {ports[10]} open ")
        except socket.error:
            print(Fore.GREEN + f"Port {ports[10]} closed ")

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
        password = input(Fore.RED + "INSTALLING THE TOOL (enter to continue): ")
        repo = "https://github.com/Simit6155/SchimmelBox-Warriors.git"
        clone_cmd = ["git", "clone", repo]
        subprocess.run(clone_cmd)
        os.chdir("SchimmelBox-Warriors")
        print(Fore.RED + "YOU NEED TO HAVE THE CLIENT.PY RUNNING ON THE SYSTEM U WANNA CONNECT TO !!! (enter to continue)")
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

    elif question == "cam":
        cam_repo = "https://github.com/techchipnet/CamPhish.git"
        cam_clone = ["git", "clone", cam_repo]
        subprocess.run(cam_clone)
        os.chdir("CamPhish")
        mod_cam = ["chmod" , "+x" , "CamPhish.sh"]
        subprocess.run(mod_cam)
        start_cam = ["./CamPhish.sh"]
        subprocess.run(start_cam)

    elif question == "osint":
        start_sherlock = ["sherlock" , "-h"]
        subprocess.run(start_sherlock)

    elif question == "support":
        webbrowser.open("https://www.instagram.com/Redsimit")
        webbrowser.open("https://discord.gg/4HJefrDyaZ")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ // ERROR HANDLING // ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    else:
        print(Fore.RED + "[~] Unknown command... ")
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
