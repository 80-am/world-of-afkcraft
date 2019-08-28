import time
import random

from random import randint
from pyautogui import press

move_keys = ['w', 'a', 'd', 'space']
run = True

print('Focus on WoW window')
for i in reversed(range(10)):
    print('Starting in ' + str(i + 1) + ' seconds!')
    time.sleep(1)

while (run):
    time_between_actions = randint(100, 900)
    inner_sleep = random.random()
    actions = randint(3, 12)

    for i in range(actions):
        press('w')
    for i in range(actions):
        random_key = [move_keys[random.randrange(len(move_keys))]
                for key in range(4)]
        press(random_key)
        time.sleep(inner_sleep)
    print('Waiting ' + str(time_between_actions) + ' seconds for next action')
    time.sleep(time_between_actions)
