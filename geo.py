# geo.py
# WORLD MONITOR CYBER FULLSCREEN
# Versi premium Termux + Hacker UI

import os
import sys
import time
import threading

URL = "https://world-monitor.app/?utm_source=chatgpt.com"

os.system("clear")

banner = r"""
██╗    ██╗ ██████╗ ██████╗ ██╗     ██████╗     
██║    ██║██╔═══██╗██╔══██╗██║     ██╔══██╗    
██║ █╗ ██║██║   ██║██████╔╝██║     ██║  ██║    
██║███╗██║██║   ██║██╔══██╗██║     ██║  ██║    
╚███╔███╔╝╚██████╔╝██║  ██║███████╗██████╔╝    
 ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═════╝     

███╗   ███╗ ██████╗ ███╗   ██╗██╗████████╗ ██████╗ ██████╗
████╗ ████║██╔═══██╗████╗  ██║██║╚══██╔══╝██╔═══██╗██╔══██╗
██╔████╔██║██║   ██║██╔██╗ ██║██║   ██║   ██║   ██║██████╔╝
██║╚██╔╝██║██║   ██║██║╚██╗██║██║   ██║   ██║   ██║██╔══██╗
██║ ╚═╝ ██║╚██████╔╝██║ ╚████║██║   ██║   ╚██████╔╝██║  ██║
╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝
"""

green = "\033[1;32m"
cyan = "\033[1;36m"
red = "\033[1;31m"
reset = "\033[0m"

print(green + banner + reset)

loading_text = [
    "[+] Initializing secure terminal...",
    "[+] Connecting global satellite...",
    "[+] Loading cyber interface...",
    "[+] Establishing encrypted channel...",
    "[+] Accessing world-monitor servers...",
    "[+] Rendering globe engine...",
    "[+] Fullscreen mode enabled..."
]

for text in loading_text:
    print(cyan + text + reset)
    time.sleep(1)

print(green + "\n[✓] SYSTEM READY\n" + reset)

# animasi terminal
def matrix():
    chars = "01"
    while True:
        line = "".join(chars[ord(os.urandom(1)) % 2] for _ in range(70))
        print(green + line + reset)
        time.sleep(0.05)

# buka browser fullscreen
def open_world():
    time.sleep(3)

    # mencoba browser fullscreen
    os.system(
        f'am start -a android.intent.action.VIEW -d "{URL}"'
    )

threading.Thread(target=matrix, daemon=True).start()
threading.Thread(target=open_world).start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print(red + "\n[!] Shutdown..." + reset)
    sys.exit()