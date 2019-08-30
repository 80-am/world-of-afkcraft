import datetime
import pyautogui
import random
import time

from random import randint
from pyautogui import press

move_keys = ['a', 'd', 'space']
auto_run_toggle = 'backspace'
run = True

print('Focus on WoW window')
for i in reversed(range(5)):
    print('Starting in ' + str(i + 1) + ' seconds!')
    time.sleep(1)

while (run):
    time_between_actions = randint(100, 900)
    inner_sleep = random.random()
    actions = randint(1, 6)
    press(auto_run_toggle)

    for i in range(actions):
        random_key = [move_keys[random.randrange(len(move_keys))]
                for key in range(4)]
        press(random_key)
        time.sleep(inner_sleep)

    press('w')
    print(datetime.datetime.now().time())
    print('Waiting ' + str(time_between_actions) + ' seconds for next action')
    time.sleep(time_between_actions)

