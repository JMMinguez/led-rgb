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


azul = "azul"
verde = "verde"
rojo = "rojo"
morado = "morado"
amarillo = "amarillo"
cyan = "cyan"
blanco = "blanco"
naranja = "naranja"
rgb = "rgb"


def encender(x, y, z):
	red.start(x)
	blue.start(y)
	green.start(z)
	input("Ejecutando hasta que se pulse una tecla")
	
def apagar():
	red.start(100)
	blue.start(100)
	green.start(100)

def encenderRGB():
	RUNNING = True
	#Ejecutara indefinidamente el modo RGB hasta que se pulse ctrl+c
	try:
		print("Ejecutando hasta que se pulse ctrl+c")
		while (RUNNING):
			red.start(100)
			blue.start(1)
			green.start(1)
			
			#Para realizar una transicion suave entre colores usaremos varios bucles for y el ChangeDutyCycle
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
		apagar()

def main():
	PROGRAMA = True
	apagar()
	
	#Se ejecutara el programa indefinidamente hasta que se cierre el programa como ctrl+c
	try:
		while (PROGRAMA):
		
			print("Elija entre los siguientes colores: rojo, azul, verde, blanco, 					amarillo, cyan, morado, naranja o rgb")
			pin = input()
			
			if pin == azul:
				#Declaramos las intensidades de cada color y va a la funcion encender
				x = 100
				y = 1
				z = 100
				encender(x, y, z)
				apagar()

			elif pin == rojo:
				x = 1
				y = 100
				z = 100
				encender(x, y, z)
				apagar()
	
			elif pin == verde:
				x = 100
				y = 100
				z = 1
				encender(x, y, z)
				apagar()
		
			elif pin == morado:
				x = 1
				y = 1
				z = 100
				encender(x, y, z)
				apagar()
	
			elif pin == cyan:
				x = 100
				y = 1
				z = 1
				encender(x, y, z)
				apagar()
	
			elif pin == amarillo:
				x = 1
				y = 100
				z = 1
				encender(x, y, z)
				apagar()

			elif pin == blanco:
				x = 1
				y = 1
				z = 1
				encender(x, y, z)
				apagar()
				
			elif pin == naranja:
				#Para modificar la intensidad del verde en este caso usamos el ChangeDutyCYcle
				red.start(1)
				blue.start(100)
				green.start(1)
				green.ChangeDutyCycle(90)
				input("Ejecutando hasta que se pulse una tecla")
				apagar()
				
			elif pin == rgb:
				encenderRGB()
	
			else:
				print("Error")
				GPIO.cleanup()
	except KeyboardInterrupt:
		PROGRAMA = False
		GPIO.cleanup()

if __name__ == "__main__":
	main()		
		
