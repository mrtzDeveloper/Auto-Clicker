from pyautogui import *
from pynput.keyboard import *
from threading import Thread

running = False

def on_press(key):
    global running
    keydata = str(key)
    if keydata.__contains__('v'):
        running = not running

def main():
    global running
    clicks = int(input('Clicks > '))
    while True:
        if running:
            mx, my = position()
            click(mx, my, clicks=clicks)

t = Thread(target=main)
t.start()

with Listener(on_press=on_press) as l:
    l.join()
