from microbit import*
import random

random.seed(1337)
while True:
    if button_a.was_pressed():
        display.show(str(random.randint(1, 6)))
    elif button_b.is_pressed():
        break
display.clear()