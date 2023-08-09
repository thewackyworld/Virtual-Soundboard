import pygame
import pygwidgets
import sys
from pygame import mixer 
import time
import random
import os

#helper from https://stackoverflow.com/questions/31836104/pyinstaller-and-onefile-how-to-include-an-image-in-the-exe-file
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


mixer.init()
#pygame.init()
bat = ['assets/battle.wav', 'assets/gensh.mp3', 'assets/dark.mp3'] 
def battle():
    rand = random.randint(0,2)
    choice = bat[rand]

    mixer.music.load(choice)
    mixer.music.play(-1)
    time.sleep(1)


def exploration():
    mixer.music.load('assets/botw.mp3')
    mixer.music.play(-1)
    time.sleep(1)

def spooky():
    mixer.music.load('assets/creep.mp3')
    mixer.music.play(-1)
    time.sleep(1)

def town():
    mixer.music.load('assets/neir.mp3')
    mixer.music.play(-1)
    time.sleep(1)


def tention():
    mixer.music.load('assets/ten.mp3')
    mixer.music.play(-1)
    time.sleep(1)

def rest():
    mixer.music.load('assets/outer.mp3')
    mixer.music.play(-1)
    time.sleep(1)


size = width, height = 650, 450

print("starting")



black = 0, 0, 0
screen = pygame.display.set_mode(size)
bwidth = 130
bheight = 130

myButton = pygwidgets.TextButton(screen, (50, 50), 'Battle', textColor=black, width=bwidth, height=bheight)
myButton1 = pygwidgets.TextButton(screen, (250, 50), 'Exploration', textColor=black, width=bwidth, height=bheight)
myButton2 = pygwidgets.TextButton(screen, (450, 50), 'Town', textColor=black, width=bwidth, height=bheight)
myButton3 = pygwidgets.TextButton(screen, (50, 250), 'Spooky', textColor=black, width=bwidth, height=bheight)
myButton4 = pygwidgets.TextButton(screen, (250, 250), 'Tention', textColor=black, width=bwidth, height=bheight)
myButton5 = pygwidgets.TextButton(screen, (450, 250), 'Rest', textColor=black, width=bwidth, height=bheight)





while True:
    for event in pygame.event.get():
        while myButton.handleEvent(event):
            battle()
        while myButton1.handleEvent(event):
            exploration()
        while myButton2.handleEvent(event):
            town()
        while myButton3.handleEvent(event):
            spooky()
        while myButton4.handleEvent(event):
            tention()
        while myButton5.handleEvent(event):
            rest()
        if event.type == pygame.QUIT: sys.exit()
        

    screen.fill('white')

    myButton.draw()
    myButton1.draw()
    myButton2.draw()
    myButton3.draw()
    myButton4.draw()
    myButton5.draw()

    pygame.display.flip()