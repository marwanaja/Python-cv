from time import sleep
import pyautogui as pt
import pyperclip as pc

sleep(2)


def move_to_text_input(message):
    position = pt.locateOnScreen('images/insta_image.png', confidence=.7)
    pt.moveTo(position[0:2], duration=.5)

move_to_text_input('hello')
