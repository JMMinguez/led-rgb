# ledRGB.py
# Practica 2. Sensores y actuadores. URJC. Julio Vega
# Ejercicio 1.1 --> encender y apagar los leds por seprado
# Autores --> Jorge Martín y Rebeca Sánchez

import time, sys
import RPi.GPIO as GPIO


def encender(pin):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin,GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)
    input("Ejecutando hasta que se pulse una tecla")
    apagar(pin)
        
def apagar(pin):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.HIGH)
    

def main():
	PROGRAMA = True
	try:
		while(PROGRAMA):
			print("Introduce un color: rojo, azul o verde")
			pin = input()
			
			if pin == "rojo" or pin == "Rojo":
				pin  = 11
				encender(pin)
			elif pin == "azul" or pin == "Azul":
				pin = 13
				encender(pin)
			elif pin == "verde" or pin == "Verde":
				pin = 15
				encender(pin)
			else:
				print("Error")	
								
			
	except KeyboardInterrupt:
		PROGRAMA = False
		GPIO.cleanup()

if __name__ == "__main__":
	main()	
# Casos de uso:
#-Introducir string no correspondiente a los colores --> ERROR y velve a pedirlo
#-Caracteres que no sean letras --> ERROR + vuleve a pedirlo
#-Si se pulsa Ctrl+C --> programa se cierra
#
