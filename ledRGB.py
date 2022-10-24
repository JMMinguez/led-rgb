# ledRGB.py
# Practica 2. Sensores y actuadores. URJC. Julio Vega
# Codigo de ejemplo de uso del LED RGB

import time, sys
import RPi.GPIO as GPIO

rojo = "rojo"
azul = "azul"
verde = "verde"

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
			print("Introduce un color: rojo, azul o")
			pin = input()
			
			if pin == rojo:
				pin  = 11
				encender(pin)
			elif pin == azul:
				pin = 13
				encender(pin)
			elif pin == verde:
				pin = 15
				encender(pin)
			else:
				print("Error")	
								
			
	except KeyboardInterrupt:
		PROGRAMA = False
		GPIO.cleanup()

if __name__ == "__main__":
	main()	
    
