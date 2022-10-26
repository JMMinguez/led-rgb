# ledRGB.py
# Practica 2. Sensores y actuadores. URJC. Julio Vega
# Codigo de ejemplo de uso del LED RGB

import time, sys
import RPi.GPIO as GPIO


GPIO.setmode (GPIO.BOARD)

GPIO.setup (11, GPIO.OUT)
GPIO.setup (13, GPIO.OUT)
GPIO.setup (15, GPIO.OUT)


rojo = GPIO.PWM (11, 100)
azul = GPIO.PWM (13, 100)
verde = GPIO.PWM (15, 100)


print("Introduce un color")

rojo.ChangeDutyCycle (1)
azul.ChangeDutyCycle (1)
verde.ChangeDutyCycle (1)

pin = input()
azuul = "azul"
rojou = "rojo"
verdeu = "verde"
morado = "morado"
blanco = "blanco"
amarillo = "amarillo"
cyan = "cyan"

if pin == azuul:
	rojo.ChangeDutyCycle(0)
	input("Ejecutando hasta que se pulse una tecla")
	GPIO.cleanup()
	
elif pin == rojou:
	encender(rojoPin)
	input("Ejecutando hasta que se pulse una tecla")
	GPIO.cleanup()
	
elif pin == verdeu:
	encender(verdePin)
	input("Ejecutando hasta que se pulse una tecla")
	GPIO.cleanup()
	
elif pin == morado:
	encender(azulPin)
	encender(rojoPin)
	input("Ejecutando hasta que se pulse una tecla")
	GPIO.cleanup()
	
elif pin == blanco:
	encender(azulPin)
	encender(rojoPin)
	encender(verdePin)
	input("Ejecutando hasta que se pulse una tecla")
	GPIO.cleanup()
	
elif pin == amarillo:
	encender(verdePin)
	encender(rojoPin)
	input("Ejecutando hasta que se pulse una tecla")
	GPIO.cleanup()
	
elif pin == cyan:
	encender(azulPin)
	encender(verdePin)
	input("Ejecutando hasta que se pulse una tecla")
	GPIO.cleanup()
	
else:
	print("Error")
	



    
