# 🌍 WORLD MONITOR CYBER FULLSCREEN - TERMUX

Dashboard globe realtime cyber fullscreen untuk Android menggunakan Termux.

Membuka:
https://world-monitor.app/?utm_source=chatgpt.com

Dengan tampilan:
- Hacker UI
- Matrix animation
- Fullscreen browser
- Cyber terminal
- Auto launch realtime globe

---

# 📦 INSTALLASI TERMUX

Download aplikasi:

- Termux
- Termux:API

## Link resmi

- :contentReference[oaicite:0]{index=0}
- :contentReference[oaicite:1]{index=1}

---

# ⚡ SETUP TERMUX

Update package:

```bash
pkg update -y && pkg upgrade -y
```

Install dependency:

```bash
pkg install python -y
pkg install termux-api -y
pkg install wget -y
```

Berikan izin storage:

```bash
termux-setup-storage
```

---

# 📥 DOWNLOAD SCRIPT

Buat file:

```bash
nano geo.py
```

Paste script `geo.py` lalu simpan:

CTRL + X

tekan:
```bash
Y
```

lalu ENTER.

---

# ▶️ MENJALANKAN SCRIPT

```bash
python geo.py
```

---

# 🖥️ FULLSCREEN MODE

Agar tampil seperti aplikasi cyber fullscreen:

Install browser fullscreen:

- :contentReference[oaicite:2]{index=2}

Atur menjadi browser default Android.

---

# ✅ TEST TERMUX API

Cek apakah API aktif:

```bash
termux-toast "TERMUX API READY"
```

Jika muncul popup Android berarti berhasil.

---

# 🔥 FITUR

- Cyber loading screen
- Matrix terminal animation
- Realtime world monitor
- Auto browser launch
- Android fullscreen support
- Hacker style interface
- Lightweight
- Support Termux Android

---

# 🚀 AUTO RUN (OPSIONAL)

Agar otomatis jalan saat membuka Termux:

Edit bashrc:

```bash
nano ~/.bashrc
```

Tambahkan:

```bash
python ~/geo.py
```

Simpan lalu restart Termux.

---

# 🛠️ TROUBLESHOOTING

## termux-open-url tidak bekerja

Pastikan:
- aplikasi `Termux:API` sudah diinstall
- semua permission Android sudah diizinkan

## Browser tidak fullscreen

Gunakan:
- Fully Kiosk Browser
- atau browser kiosk mode lainnya

---

# 👨‍💻 AUTHOR

CYBER WORLD MONITOR TERMUX EDITION

Realtime Globe Intelligence Dashboard
