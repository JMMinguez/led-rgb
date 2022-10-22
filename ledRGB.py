# ledRGB.py
# Practica 2. Sensores y actuadores. URJC. Julio Vega
# Codigo de ejemplo de uso del LED RGB

import time, sys
import RPi.GPIO as GPIO

rojoPin = 11
azulPin = 13
verdePin = 15

def encender(pin):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin,GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)
        
def apagar(pin):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.HIGH)
    
def encenderRojo():
    encender(verdePin)

print("Introduce un color")

encenderRojo()
input("Ejecutando hasta que se pulse una tecla")
apagar(rojoPin)
GPIO.cleanup()
    
