import speech
from microbit import sleep

speech.say("I can sing!")
sleep(1000)
speech.say("Listen to me!")
sleep(1000)

speech.pronounce("AEAE/HAEMM", pitch=200, speed=100)
sleep(1000)

solfa = [
    "#115DOWWWWWW",
    "#103REYYYYYY",
    "#94MIYYYYYY",
    "#88FAOAOAOAOR",
    "#78SOHWWWWW",
    "#70LAOAOAOAOR",
    "#62TIYYYYYY",
    "#58DOWWWWWW",
]


song = ''.join(solfa)
speech.sing(song, speed=100)
solfa.reverse()
song = ''.join(solfa)
speech.sing(song, speed=100)