# ledRGB.py
# Practica 2. Sensores y actuadores. URJC. Julio Vega
# Ejercicio 1.2 --> encender y apagar nueve colores diferentes
# Autores --> Jorge Martín y Rebeca Sánchez

import time, sys
import RPi.GPIO as GPIO

led_rojo = 11
led_azul = 13
led_verde = 15
TOPE = 1
MIN = 100

GPIO.setmode(GPIO.BOARD)
GPIO.setup(led_rojo, GPIO.OUT)
GPIO.setup(led_azul, GPIO.OUT)
GPIO.setup(led_verde, GPIO.OUT)

red = GPIO.PWM(led_rojo, 500)
blue = GPIO.PWM(led_azul, 500)
green = GPIO.PWM(led_verde, 500)


def encender(x, y, z):
	red.start(x)
	blue.start(y)
	green.start(z)
	input("Ejecutando hasta que se pulse una tecla")
	
def apagar():
	red.start(MIN)
	blue.start(MIN)
	green.start(MIN)

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
		
			print("Elija entre los siguientes colores: rojo, azul, verde, blanco, amarillo, cyan, morado, naranja o rgb")
			pin = input()
			
			if pin == "azul":
				#Declaramos las intensidades de cada color y va a la funcion encender
				encender(MIN, TOPE, MIN)
				apagar()

			elif pin == "rojo":
				encender(TOPE, MIN, MIN)
				apagar()
	
			elif pin == "verde":
				encender(MIN, MIN, TOPE)
				apagar()
		
			elif pin == "morado":
				encender(TOPE, TOPE, MIN)
				apagar()
	
			elif pin == "cyan":
				encender(MIN, TOPE, TOPE)
				apagar()
	
			elif pin == "amarillo":
				encender(TOPE, MIN, TOPE)
				apagar()

			elif pin == "blanco":
				encender(TOPE, TOPE, TOPE)
				apagar()
				
			elif pin == "naranja":
				#Para modificar la intensidad del verde en este caso usamos el ChangeDutyCYcle
				red.start(TOPE)
				blue.start(MIN)
				green.start(TOPE)
				green.ChangeDutyCycle(90)
				input("Ejecutando hasta que se pulse una tecla")
				apagar()
				
			elif pin == "rgb":
				encenderRGB()
	
			else:
				print("Error")
				
	except KeyboardInterrupt:
		PROGRAMA = False
		GPIO.cleanup()

if __name__ == "__main__":
	main()		

#Casos de uso:
#-Colores erróneos --> ERROR + volver a pedir
#-Caracteres que no sean letras --> ERROR + volver a pedir
#
