from microbit import*

while True:
    reading = accelerometer.get_x()
    if reading > 20:
        display.scroll("R")
    elif reading < -20:
        display.scroll("L")
    else:
        display.scroll("-")

