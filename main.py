import pyautogui as pg
import sys
from pynput import keyboard

if len(sys.argv) == 1:
    print("Coordenadas nao informadas")
    exit(0)

def kill_command():
    pg.hotkey('ctrl', 'c')


def on_release(key):
    if key == keyboard.Key.esc:
        print("Saindo...")
        pg.click(1143,625)
        pg.hotkey('ctrl', 'c')


mouseCoord = sys.argv[1:3]

listener = keyboard.Listener(on_release=on_release)
listener.start()


pg.click(mouseCoord)


with open('./shrek.txt',encoding='latin-1',mode='r') as text:
    for line in text:
        if(line != ""):
            pg.write(line)
            pg.press("Enter")
