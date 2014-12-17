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
#import time
import picamera
from random import choice

#Setup Pygame
pygame.init()
pygame.mixer.init()

#Setup the GPIO to use the logical pin numbering
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

#Create Variables
global distance

LED1 = 8
LED2 = 10
LED3 = 12
LED4 = 16
LED5 = 18
LED6 = 22
LED7 = 24

red = 36
blue = 38
green = 40
delay = 0.2
camera = picamera.PiCamera()

trigger = 26
echo = 23

song1 = "./jingle.mp3"
song2 = "./white.mp3"
song3 = "./merry.mp3"

#Setup GPIO pins

GPIO.setup(LED1, GPIO.OUT)
GPIO.setup(LED2, GPIO.OUT)
GPIO.setup(LED3, GPIO.OUT)
GPIO.setup(LED4, GPIO.OUT)
GPIO.setup(LED5, GPIO.OUT)
GPIO.setup(LED6, GPIO.OUT)
GPIO.setup(LED7, GPIO.OUT)
GPIO.setup(trigger, GPIO.OUT)

GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)

GPIO.setup(echo, GPIO.IN)

#Define Functions

def ultra(sensor):
    global distance
    if sensor == 0:

        time.sleep(0.3)
        signaloff = 0
        signalon = 0
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
	pygame.mixer.music.load(x)
	pygame.mixer.music.play(1)

def flash(a,b,c,d,e,f,g):
		GPIO.output(a, True)
		GPIO.output(b, False)
		GPIO.output(c, True)
		GPIO.output(d, False)
		GPIO.output(e, True)
		GPIO.output(f, False)
		GPIO.output(g, True)		
		time.sleep(0.2)
		GPIO.output(a, False)
		GPIO.output(b, True)
		GPIO.output(c, False)
		GPIO.output(d, True)
		GPIO.output(e, False)
		GPIO.output(f, True)
		GPIO.output(g, False)
		time.sleep(0.2)

def rgb():
	GPIO.output(red, True)
	GPIO.output(blue, False)
	GPIO.output(green, False)
	time.sleep(delay)
	GPIO.output(red, False)
	GPIO.output(blue, True)
	GPIO.output(green, False)
	time.sleep(delay)
	GPIO.output(red, False)
	GPIO.output(blue, False)
	GPIO.output(green, True)
	time.sleep(delay)
	GPIO.output(red, False)
	GPIO.output(blue, False)
	GPIO.output(green, False)
	time.sleep(delay)

def reset(red,green,blue,a,b,c,d,e,f,g):
	GPIO.output(red, False)
	GPIO.output(blue, False)
	GPIO.output(green, False)
	GPIO.output(a, False)
	GPIO.output(b, False)
	GPIO.output(c, False)
	GPIO.output(d, False)
	GPIO.output(e, False)
	GPIO.output(f, False)
	GPIO.output(g, False)

#Main Body Of Code

#Cue to tell me that the system is ready
music("./sleigh.mp3")
reset(red,green,blue,LED1,LED2,LED3,LED4,LED5,LED6,LED7)


while True:
	ultra(0)
	songlist = [song1,song2,song3]
	chosen = choice(songlist)
	if distance < 30:
		a = datetime.datetime.now()
		a = str(a)
		a = a[0:19]
		alert = ("Santa detected at "+str(a))
		print(alert)
		pic = (a)+(".jpg")
		camera.resolution = (1024, 768)
		camera.capture(pic)
		music(chosen)
		for i in range(100):
			flash(LED1,LED2,LED3,LED4,LED5,LED6,LED7)
			rgb()
		time.sleep(1)
		reset(red,green,blue,LED1,LED2,LED3,LED4,LED5,LED6,LED7)
	else:
		print("Waiting for Santa")
		time.sleep(1)
