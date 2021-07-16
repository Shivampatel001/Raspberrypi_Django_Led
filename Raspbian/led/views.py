from django.shortcuts import render,HttpResponse
import os
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from time import sleep # Import the sleep function from the time module
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW) # Set pin 8 to be an output pin and set initial value to low (off)

def index(request):
    return render(request,'index.html')

def turn_on(request):
    GPIO.output(8, GPIO.HIGH) # Turn on
    return render(request,'index.html')



def turn_off(request):
    GPIO.output(8, GPIO.LOW) # Turn off
    return render(request,'index.html')

