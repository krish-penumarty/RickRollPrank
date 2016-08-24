#!/usr/bin/python
import time
import webbrowser
import random

i = 0
while i < 3:
    randomTime = random.randint(10, 20)
    time.sleep(randomTime * 60)
    webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    i = i + 1

