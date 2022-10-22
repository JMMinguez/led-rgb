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
    


print("Introduce un color")
pin = input()
azul = "azul"
rojo = "rojo"
verde = "verde"

if pin == azul:
	encender(azulPin)
elif pin == rojo:
	encender(rojoPin)
elif pin == verde:
	encender(verdePin)
else:
	print("")
	


input("Ejecutando hasta que se pulse una tecla")
GPIO.cleanup()
    
