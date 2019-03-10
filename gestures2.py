from microbit import*
import random
answers = ["who knows", "I Think itll happen", "Go for it",
           "DEFINATLY", "NO DONT", "Eh"]

while True:
    display.scroll("8")
    if accelerometer.was_gesture("shake"):
        display.clear()
        sleep(1000)
        display.show(random.choice(answers))
