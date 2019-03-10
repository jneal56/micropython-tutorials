from microbit import*

while True:
    gesture = accelerometer.current_gesture()
    if gesture == "face up":
        display.show(Image.HAPPY)
    elif gesture == "face down":
        display.show(Image.ASLEEP)
    else:
        display.show(Image.SURPRISED)