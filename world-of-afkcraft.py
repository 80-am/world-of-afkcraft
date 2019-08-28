import time
import random

from random import randint
from pyautogui import press

move_keys = ['w', 'a', 'd', 'space']
print('[1] Random movement')
print('[2] Attack mode')
mode = int(input('Select afk-mode: '))
run = True

print('Focus on WoW window')
for i in reversed(range(10)):
    print('Starting in ' + str(i) + ' seconds!')
    time.sleep(1)

while (run):
    time_between_actions = randint(100, 900)
    inner_sleep = random.random()
    actions = randint(3, 12)

    if (mode == 1):
        for i in range(actions):
            press('w')
        for i in range(actions):
            random_key = [move_keys[random.randrange(len(move_keys))]
                    for key in range(4)]
            press(random_key)
            time.sleep(inner_sleep)
        print('Waiting ' + str(time_between_actions) + ' seconds for next action')
        time.sleep(time_between_actions)
    
    if (mode == 2):
        for i in range(actions):
            press('tab')
            press('t')
            for i in range(5):
                attack_speed = randint(2, 5)
                press('1')
                print('Attacking in ' + str(attack_speed) + ' seconds')
                time.sleep(attack_speed)
            
        print('Waiting ' + str(time_between_actions) + ' seconds for next action')
        time.sleep(time_between_actions)

