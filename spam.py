import time
from pynput.keyboard import Key, Controller

kb = Controller()

print("YOU HAVE 10 SECONDS!")

time.sleep(10)

while(True):
    time.sleep(2)
    kb.press('w')
    kb.release('w')
    kb.press(Key.enter)
    kb.release(Key.enter)
