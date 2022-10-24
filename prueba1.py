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

def encender(x, y, z):
	red.start(x)
	blue.start(y)
	green.start(z)
	input("Ejecutando hasta que se pulse una tecla")
	GPIO.cleanup()

def encenderRGB():
	RUNNING = True
	try:
		while (RUNNING):
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
	except KeyboardInterrupt:
		RUNNING = False
		GPIO.cleanup()

def main():
	if pin == azul:
		x = 100
		y = 1
		z = 100
		encender(x, y, z)
	

	elif pin == rojo:
		x = 1
		y = 100
		z = 100
		encender(x, y, z)
	
	elif pin == verde:
		x = 100
		y = 100
		z = 1
		encender(x, y, z)
		
	elif pin == morado:
		x = 1
		y = 1
		z = 100
		encender(x, y, z)
	
	elif pin == cyan:
		x = 100
		y = 1
		z = 1
		encender(x, y, z)
	
	elif pin == amarillo:
		x = 1
		y = 100
		z = 1
		encender(x, y, z)

	elif pin == blanco:
		x = 1
		y = 1
		z = 1
		encender(x, y, z)
	
	elif pin == rgb:
		encenderRGB()
	
	else:
		print("Error")
		GPIO.cleanup()

if __name__ == "__main__":
	main()		
		
