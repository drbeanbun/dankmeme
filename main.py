from pynput.keyboard import Key, Controller
import time


commands = ["pls beg","pls dep max","pls hunt","pls postmemes","pls fish"]
keyboard = Controller()
time.sleep(10)
x = 0
while x < 1000:
    for char in commands[0]:
        keyboard.press(char)
        keyboard.release(char)
    keyboard.press(Key.enter)
    for char in commands[2]:
        keyboard.press(char)
        keyboard.release(char)
    keyboard.press(Key.enter)
    for char in commands[2]:
        keyboard.press(char)
        keyboard.release(char)
    keyboard.press(Key.enter)
    time.sleep(20)
    for char in commands[3]:
        keyboard.press(char)
        keyboard.release(char)
    keyboard.press(Key.enter)
    time.sleep(2)
    keyboard.press("n")
    keyboard.press(Key.enter)
    for char in commands[1]:
        keyboard.press(char)
        keyboard.release(char)
    keyboard.press(Key.enter)
    time.sleep(41)
    x += 1


