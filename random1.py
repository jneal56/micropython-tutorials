from microbit import*
import random

names = ["Dalton", "Flacco", "Carr", "Manning", "Mayfield", "Rivers"]
while True:
    if button_a.is_pressed():
        display.scroll(random.choice(names))
    elif button_b.was_pressed():
        display.show(str(random.randint(1,9)))

    elif pin2.is_touched():
        answer = random.randrange(100) + random.random()
        display.show(str(answer))