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
        print(Fore.RED + "               ██████╗ ███████╗██████╗ ███████╗██╗███╗   ███╗██╗████████╗")
        print(Fore.RED + "               ██╔══██╗██╔════╝██╔══██╗██╔════╝██║████╗ ████║██║╚══██╔══╝")
        print(Fore.RED + "               ██████╔╝█████╗  ██║  ██║███████╗██║██╔████╔██║██║   ██║   ")
        print(Fore.RED + "               ██╔══██╗██╔══╝  ██║  ██║╚════██║██║██║╚██╔╝██║██║   ██║   ")
        print(Fore.RED + "               ██║  ██║███████╗██████╔╝███████║██║██║ ╚═╝ ██║██║   ██║   ")
        print(Fore.RED + "               ╚═╝  ╚═╝╚══════╝╚═════╝ ╚══════╝╚═╝╚═╝     ╚═╝╚═╝   ╚═╝   ")
        print(Fore.RED + "                               Made by @redsimit ")

    redsimit()

    question = input(Fore.GREEN + """
Avaible commands: ═════════════════════╗═══════════════════════════════════════╗
╚═ Networking:                         ╚═ Attacking:                           ╚═ Other:
  ╚═ m port = scans multiple ports       ╚═  spam = spammbot                     ╚═ q = quit
     s port = scans single port              rat = reverse shell //kali             support
     osint = info gathering //kali           fish = phishing //kali   
     call = calls anonym //BETA              cam = webcam hacker //kali
     geo = opens geolocator                  alhack = another multi tool //kali
                            
enter command: """)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def clear():
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ // MAIN // ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    if question == "geo":
        clear()
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
        clear()
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
        clear()
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


        print(Fore.LIGHTGREEN_EX + "                                                                This Multi-Port tester was made by @Redsimit ")
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
        clear()
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
            time.sleep(int(speed))

    elif question == "rat":
        clear()
        password = input(Fore.RED + "INSTALLING THE TOOL (enter to continue): ")
        repo = "https://github.com/Simit6155/SchimmelBox-Warriors.git"
        clone_cmd = ["git", "clone", repo]
        subprocess.run(clone_cmd)
        os.chdir("SchimmelBox-Warriors")
        print(Fore.RED + "YOU NEED TO HAVE THE CLIENT.PY RUNNING ON THE SYSTEM U WANNA CONNECT TO !!! (enter to continue)")
        time.sleep(3)
        subprocess.run(["python3", "server.py"])

    elif question == "fish":
        clear()
        phish_repo = "https://github.com/htr-tech/zphisher.git"
        phish_clone = ["git", "clone", phish_repo]
        subprocess.run(phish_clone)
        os.chdir("zphisher")
        mod_phish = ["chmod" , "+x" , "zphisher.sh"]
        subprocess.run(mod_phish)
        start_phish = ["./zphisher.sh"]
        subprocess.run(start_phish)

    elif question == "cam":
        clear()
        cam_repo = "https://github.com/techchipnet/CamPhish.git"
        cam_clone = ["git", "clone", cam_repo]
        subprocess.run(cam_clone)
        os.chdir("CamPhish")
        mod_cam = ["chmod" , "+x" , "CamPhish.sh"]
        subprocess.run(mod_cam)
        start_cam = ["./CamPhish.sh"]
        subprocess.run(start_cam)

    elif question == "osint":
        clear()
        start_sherlock = ["sherlock" , "-h"]
        subprocess.run(start_sherlock)

    elif question == "support":
        clear()
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

    elif question == "call":
        clear()
        import webbrowser
        import colorama
        import requests
        from colorama import Fore, init
        import pyautogui
        import time

        init(autoreset=True)

        print(Fore.RED + """
        ▄▄▄·    ▄▄·  ▄▄▄· ▄▄▌  ▄▄▌  ▄▄▄ .▄▄▄  
        ▐█ ▄█   ▐█ ▌▪▐█ ▀█ ██•  ██•  ▀▄.▀·▀▄ █·
         ██▀·   ██ ▄▄▄█▀▀█ ██▪  ██▪  ▐▀▀▪▄▐▀▀▄ 
        ▐█▪·•   ▐███▌▐█ ▪▐▌▐█▌▐▌▐█▌▐▌▐█▄▄▌▐█•█▌
        .▀    ▀ ·▀▀▀  ▀  ▀ .▀▀▀ .▀▀▀  ▀▀▀ .▀  ▀""")

        print(Fore.RED + "~~~~ Author @Redsimit ~~~~ ")


        def phone_call():
            number = input(Fore.GREEN + "Enter number: ")
            print(Fore.GREEN + "Calling dont move your mouse . . . . ")
            webbrowser.open("https://callmyphone.org")
            time.sleep(5)
            pyautogui.leftClick(902, 389)
            time.sleep(1)
            pyautogui.typewrite(number)
            time.sleep(0.5)
            pyautogui.leftClick(1257, 389)


        phone_call()

        callagain = input(Fore.GREEN + "Call again? y/n ")
        if callagain.lower() == "y":
            phone_call()
        elif callagain.lower() == "n":
            print(Fore.GREEN + "Closing . . . .")
            time.sleep(1)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ // ERROR HANDLING // ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  
    else:
        print(Fore.RED + "[~] Unknown command... ")
      
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
