# tiktok_gesture.py
# TIKTOK GESTURE CONTROL - TERMUX ANDROID EDITION

import cv2
import mediapipe as mp
import os
import time

TIKTOK_URL = "https://www.tiktok.com/"

# buka tiktok web
os.system(f'am start -a android.intent.action.VIEW -d "{TIKTOK_URL}"')

print("""
=========================================
     TIKTOK GESTURE CONTROL
=========================================

1 JARI  = NEXT VIDEO
2 JARI  = PREVIOUS VIDEO
3 JARI  = VOLUME UP

Tekan Q untuk keluar
=========================================
""")

time.sleep(5)

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("[!] Kamera tidak ditemukan")
    exit()

last_action = time.time()

with mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
) as hands:

    while True:
        success, frame = cap.read()

        if not success:
            break

        frame = cv2.flip(frame, 1)

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        result = hands.process(rgb)

        fingers = 0

        if result.multi_hand_landmarks:

            for hand_landmarks in result.multi_hand_landmarks:

                lm = hand_landmarks.landmark

                # index
                if lm[8].y < lm[6].y:
                    fingers += 1

                # middle
                if lm[12].y < lm[10].y:
                    fingers += 1

                # ring
                if lm[16].y < lm[14].y:
                    fingers += 1

                mp_draw.draw_landmarks(
                    frame,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS
                )

            now = time.time()

            # delay anti spam
            if now - last_action > 2:

                # 1 jari = next video
                if fingers == 1:
                    print("[+] NEXT VIDEO")

                    os.system(
                        "input swipe 500 1600 500 300"
                    )

                    last_action = now

                # 2 jari = previous
                elif fingers == 2:
                    print("[+] PREVIOUS VIDEO")

                    os.system(
                        "input swipe 500 300 500 1600"
                    )

                    last_action = now

                # 3 jari = volume up
                elif fingers == 3:
                    print("[+] VOLUME UP")

                    os.system(
                        "input keyevent 24"
                    )

                    last_action = now

        cv2.putText(
            frame,
            f"FINGERS: {fingers}",
            (10, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )

        cv2.imshow("TikTok Gesture Control", frame)

        key = cv2.waitKey(1)

        if key == ord("q"):
            break

cap.release()
cv2.destroyAllWindows()
