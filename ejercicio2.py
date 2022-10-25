# ledRGB.py
# Practica 2. Sensores y actuadores. URJC. Julio Vega
# Codigo de ejemplo de uso del LED RGB

import time, sys
import RPi.GPIO as GPIO

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

	
x = 100
y = 100
z = 100

def onoff(x, y, z):
	red.start(x)
	blue.start(y)
	green.start(z)

	
def config(color, valor):
	global x
	global y
	global z
	
	x = x
	y = y
	z = z
	
	#Dependiendo de si se desea encender o apagar un color, la funcion asignara un valor 1 o 100 a los colores primarios que participen en el color deseado
	if color == "rojo":
		x = valor
			
	elif color == "azul":
		y = valor
	elif color == "verde":
		z = valor
	elif color == "morado":
		x = valor
		y = valor
	elif color == "cyan":
		y = valor
		z = valor
	elif color == "amarillo":
		x = valor
		z = valor
	elif color == "blanco":
		x = valor
		y = valor
		z = valor
	else:
		ERROR = True
		
def main():
	PROGRAMA = True
	
	red.start(100)
	blue.start(100)
	green.start(100)

	try:
		while(PROGRAMA):
			
			ERROR = False
			print("Introduce una accion (encender o apagar) seguido de un color (rojo, azul, verde, morado, cyan, amarillo o blanco)")
			msg = input()
			#Separamos el msg en dos partes, accion y color
			orden = msg.split()
			accion = orden[0]
			color = orden[1]
				
			if accion == "encender":
				valor = 1
				config(color, valor)
				if ERROR == True:
					print("Color erroneo")
				else:
					onoff(x, y, z)
		
			elif accion == "apagar":
				valor = 100
				config(color, valor)
				if ERROR == True:
					print("Color erroneo")
				else:
					onoff(x, y, z)
			else:
				print("accion erronea")
	except KeyboardInterrupt:
		PROGRAMA = False
		GPIO.cleanup()

if __name__ == "__main__":
	main()		
		
    
	
