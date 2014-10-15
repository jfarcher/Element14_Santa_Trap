"""
Element 14 Holiday Project
Python / Raspberry Pi Powered Christmas Tree and Santa Trap.

Ultrasonic trigger
Plays music via Pygame
Flash lights while music is playing
Triggers Pi Noir to take a picture, ready to catch Santa!



All code is released under the GPL v3 Licence, enjoy hacking!

les
@biglesp
bigl.es
"""
#Import Modules
import time
import datetime
import RPi.GPIO as GPIO
import pygame
import time
import picamera
from random import choice

#Setup Pygame
pygame.init()
pygame.mixer.init()

#Create Variables
global distance

song1 = "Link to music"
song2 = "Link to music"
song3 = "Link to music"

LED1 = 1
LED2 = 2
LED3 = 3
LED4 = 4

camera = picamera.PiCamera()

#Create List which we will use to play a *random* song

music = ["song1","song2","song3"]

#Define Functions

def ultra(sensor):
    global distance
    if sensor == 0:

        time.sleep(0.3)

        GPIO.output(trigger, True)

        time.sleep(0.00001)
        GPIO.output(trigger, False)
        while GPIO.input(echo) == 0:
          signaloff = time.time()
        while GPIO.input(echo) == 1:
          signalon = time.time()

        timepassed = signalon - signaloff

        distance = timepassed * 17000
        
        return distance

    else:
        print "Error."

def music(x):
	pygame.mixer.music.load("/home/les/Music/jingle.ogg")
	pygame.mixer.music.play(1)

#Main Body Of Code



while True:
	ultra(0)
	if distance < 30:

	    a = datetime.datetime.now()
	    a = str(a)
	    a = a[0:19]
	    alert = ("Santa detected at "+str(a))
	    print(alert)
	    pic = (a)+(".jpg")
	    vid = (a)+(".h264")
	    message = (alert),(pic),(vid)
	    camera.resolution = (1024, 768)
	    camera.capture(pic)
	    time.sleep(10)
	else:

