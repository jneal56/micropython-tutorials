from microbit import*

while True:
    if pin0.is_touched():
        display.show(Image.SURPRISED)
    elif pin2.is_touched():
        break
    else:
        display.show(Image.HAPPY)
display.clear()