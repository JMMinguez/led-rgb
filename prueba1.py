# ledRGB.py
# Practica 2. Sensores y actuadores. URJC. Julio Vega
# Codigo de ejemplo de uso del LED RGB

import time, sys
import RPi.GPIO as GPIO
run = True

led_rojo = 11
led_azul = 13
led_verde = 15

GPIO.setmode(GPIO.BOARD)
GPIO.setup(led_rojo, GPIO.OUT)
GPIO.setup(led_azul, GPIO.OUT)
GPIO.setup(led_verde, GPIO.OUT)

red = GPIO.PWM(led_rojo, 500)
blue = GPIO.PWM(led_azul, 500)
green = GPIO.PWM(led_verde, 500)

print("Elija entre los siguientes colores: rojo, azul, verde, blanco, amarillo, cyan, morado o rgb")
pin = input()
azul = "azul"
verde = "verde"
rojo = "rojo"
morado = "morado"
amarillo = "amarillo"
cyan = "cyan"
blanco = "blanco"
rgb = "rgb"


if pin == azul:
	red.start(100)
	blue.start(1)
	green.start(100)
	input("Ejecutando hasta que se pulse una tecla")
	GPIO.cleanup()

elif pin == rojo:
	red.start(1)
	blue.start(100)
	green.start(100)
	input("Ejecutando hasta que se pulse una tecla")
	GPIO.cleanup()
	
elif pin == verde:
	red.start(100)
	blue.start(100)
	green.start(1)
	input("Ejecutando hasta que se pulse una tecla")
	GPIO.cleanup()
	
elif pin == morado:
	red.start(1)
	blue.start(1)
	green.start(100)
	input("Ejecutando hasta que se pulse una tecla")
	GPIO.cleanup()
	
elif pin == cyan:
	red.start(100)
	blue.start(1)
	green.start(1)
	input("Ejecutando hasta que se pulse una tecla")
	GPIO.cleanup()
	
elif pin == amarillo:
	red.start(1)
	blue.start(100)
	green.start(1)
	input("Ejecutando hasta que se pulse una tecla")
	GPIO.cleanup()

elif pin == blanco:
	red.start(1)
	blue.start(1)
	green.start(1)
	input("Ejecutando hasta que se pulse una tecla")
	GPIO.cleanup()
	
elif pin == rgb:
	while (True):
		red.start(100)
		blue.start(1)
		green.start(1)
		
		for x in range(1,101):
			green.ChangeDutyCycle(x)
			time.sleep(0.025)
		
		for x in range(1,101):
			red.ChangeDutyCycle(101-x)
			time.sleep(0.025)
			
		for x in range(1,101):
			green.ChangeDutyCycle(101-x)
			blue.ChangeDutyCycle(x)
			time.sleep(0.025)
		
		for x in range(1,101):
			red.ChangeDutyCycle(x)
			time.sleep(0.025)

else:
	print("Error")
	GPIO.cleanup()
					
		
