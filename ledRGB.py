# ledRGB.py
# Practica 2. Sensores y actuadores. URJC. Julio Vega
# Codigo de ejemplo de uso del LED RGB

import time, sys
import RPi.GPIO as GPIO

rojo = 11
azul = 13
verde = 15

rojo = "rojo"
azul = "azul"
verde = "verde"

def encender(pin):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin,GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)
        
def apagar(pin):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.HIGH)
    

def main():
	PROGRAMA = True
	try:
		while(PROGRAMA):
			print("Introduce un color")
			pin = input()
			
			if pin == rojo:
				pin  = 11
			elif pin == azul:
				pin = 13
			elif pin == verde:
				pin = 15
			else:
				print("Error")
				GPIO.cleanup()	
					
			encender(pin)
			input("Ejecutando hasta que se pulse una tecla")
			apagar(pin)
			
	except KeyboardInterrupt:
		PROGRAMA = False
		GPIO.cleanup()

if __name__ == "__main__":
	main()	
    
