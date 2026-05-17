# cctv.py
# INDONESIA LIVE CCTV DASHBOARD - TERMUX EDITION

import webbrowser
import os
import time

os.system("clear")

banner = r"""
 ██████╗ ██████╗████████╗██╗   ██╗
██╔════╝██╔════╝╚══██╔══╝██║   ██║
██║     ██║        ██║   ██║   ██║
██║     ██║        ██║   ╚██╗ ██╔╝
╚██████╗╚██████╗   ██║    ╚████╔╝
 ╚═════╝ ╚═════╝   ╚═╝     ╚═══╝

INDONESIA REALTIME CCTV
"""

print(banner)

cities = {
    "1": ("Jakarta", "https://www.atcs-jakarta.com/"),
    "2": ("Bandung", "https://atcsindonesia.com/kamera/cctv-jawa-barat"),
    "3": ("Surabaya", "https://atcs.surabaya.go.id/"),
    "4": ("Semarang", "https://dishub.semarangkota.go.id/atcs"),
    "5": ("Yogyakarta", "https://atcs.jogjakota.go.id/"),
    "6": ("Bali", "https://atcs.denpasarkota.go.id/"),
    "7": ("Makassar", "https://atcs.makassarkota.go.id/"),
    "8": ("Medan", "https://dishub.pemkomedan.go.id/atcs"),
    "9": ("Batam", "https://atcs.batam.go.id/"),
    "10": ("Sukabumi", "https://atcsindonesia.com/")
}

print("===================================")
print("   LIVE CCTV KOTA BESAR INDONESIA ")
print("===================================\n")

for key, value in cities.items():
    print(f"[{key}] {value[0]}")

print("\n[0] Exit\n")

choice = input("Pilih kota CCTV : ")

if choice == "0":
    print("Keluar...")
    exit()

if choice in cities:
    city, url = cities[choice]

    print(f"\n[+] Membuka CCTV realtime {city}...")
    time.sleep(2)

    # buka browser Android fullscreen
    os.system(f'am start -a android.intent.action.VIEW -d "{url}"')

    print("[+] CCTV dashboard launched.")
else:
    print("[!] Pilihan tidak valid.")
