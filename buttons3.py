from microbit import*

while True:
    if button_a.is_pressed() and button_b.is_pressed():
        break
    elif button_a.is_pressed():
        display.show(Image.HAPPY)
    elif button_b.is_pressed():
        display.show(Image.COW)
    else:
        display.show(Image.SAD)
display.scroll("I'm going to bed now", delay = 70)
display.clear()