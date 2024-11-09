import pyautogui
import time

def anozys_auto_clicker(interval):
    try:
        print('Anozys Auto Clicker en cours d\'utilisation\nAppuie sur  CTRL+C pour stopper...')
        while True:
            pyautogui.click()   #click gauche
            time.sleep(interval)
    except KeyboardInterrupt:
        print('\n\n Anozys auto Clicker est arrêté.')

# Interval de click
interval = float(input("Tu veux un click tout les combien de temps ?\n Temps en seconde : "))
anozys_auto_clicker(interval)