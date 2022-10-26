# p2-gpio-ledrgb

## 1. Introducción
En esta segunda práctica vamos a utilizar un LED más avanzado al de la práctica 1, un **LED RGB**. Este LED contiene en una solapieza los tres colores primarios, y modulándolos convenientemente podremos conseguir cualquier color de luz.
## 2. Los pines GPIO
Estos pines se utilizan comúnmente para conectar dispositivos electrónicos como sensores y actuadores.
Estos pines son digitales y que se pueden configurar de entrada o de salida. Si se activan como salida se activan o desactivan por código, es decir, pueden ponerse a 1 (HIGH) o a 0 (LOW) ; si se activan como entrada oueden leer datos binarios, 1 si hay señal de voltaje o 0 si no hay.
Los puertos GPIO funcionan sobre niveles lógicos de 3,3V , el 0V significa el 0 lógico (LOW) y 3,3 equivale al 1 lógico (HIGH). Hay que tener cuidado de no conectarlos a la alimentación de 5V y 3,3V directamente.

Para el uso de los pines como **ìn de entrada**, se puede configurar de dos maneras: como evento/interrupción para que genere alguna acción sobre el sistema oque la acción sea realizada cuando uno o más pines sean activados por algún sensor.
Los pines GPIO son capaces de proporcionar un máximo de *50mA* al mismo tiempo, aunque no existe un limitador y no pasa nada si nos pasamos ligeramente de ese valor en un momento dado. 

Terminar//


![Imagen resistencias](https://github.com/rsanchez2021/Image/blob/main/resistencia_p2_sensores.png 'Resistencias utilizadas')

## 5. Ejercicios
En esta práctica utilizaremos pos pines: 11 , 13 y 15, además del pin 1 para el GND. El circuito quedaría:

![Circuio p2](https://github.com/rsanchez2021/Image/blob/main/circuito_p2_sensores.png 'Circuito p2')

### Ejercicio 1.1
Para este primer ejercicio se ha utilizado las intrucciones: 
```python
GPIO.setmode(GPIO.BOARD)
GPIO.setup()
GPIO.output()
```
Esto se debe a que como solo hay que encender los leds sin tener que calcular intensidades es más sencillo poniendo solo si están encendidos o apagados. Además, se ha añadido un try/except  dentro del while para poder salir del programa haciendo Ctrl+C.
```python
except keyboardInterrupt:
	PROGRAMA = Flase
	GPIO.cleanup()
```
**Casos de uso**
-Introducir string no correspondiente a los colores (rojo ó Rojo) sale un ERROR y vuelve a pedirlo.
-Introducir caracteres que no sean letras también vuelve a introducirlo.
-Si se pulse Ctrl+C se cierra el programa pero antes hace un *GPIO.cleanup* para que no se queden encendidos los leds.

### Ejercicio 1.2
En este ejercicio, ya no nos vale con encender y apagar leds, pues necesitamos más de cuatro colores. Para ello, hemos cambiado las funciones de encender y apagar  para que utilice el comando **pwm.star()** para cada color. Por ejemplo, si el color que queremos encender es el naranja, el azul se apaga (100), el led rojo se enciende lo máximo que puede (1) y el led verde se enciende a un 90%. Haciendo esto se podría sacar cualquier color que queramos con el comando **pin.ChangeDutyCycle()**
También se ha añadido un modo de led RGB que va cambiando constantemente de color . Esto lo hace empezando con un ciclo de trabajo de 100 y va disminuyendo de uno a uno hasta que se enciende el siguiente led. 
**Casos de uso**
-Si se introducen colores erroneos sale un ERROR
-Caractéres que no sean letras también sale un error.

Se proporcionan el encendido de los led rojo y verde:

![gif led rojo](https://github.com/rsanchez2021/Image/blob/main/6yc8v0.gif 'gif led rojo')
![gif led verde](https://github.com/rsanchez2021/Image/blob/main/6yc8rb.gif 'gif led verde')

### Ejercicio 2
Para el segundo ejercicio, hemos diferenciado dos funciones diferentes más el main. En la primera hemos unificado las funciones encender y apagar en una sola para luego solo tener que poner el valor (1 si quiero encender y 100 si quiero apagarlo). En la segunda función se establecen los valores en determinados leds pero manteniendo los valores que no se modifican, es decir, si quieres encender el rojo mientras está el azul encendido, este último se va a mantener así. Finalmente, en el *main* lo primero que se hace es meter las acción y el color, esto se mete en una tupla para separaren dos:
```python
msg = input()
orden = msg.split()
accion = orden[0]
color = orden[1]
```
Además se ha añadido un if para que si la acción es “salir” se hace *break*y se cierra el programa.

**Casos de uso**
- Si se introducen acciones que no sean apagar, encender o salir o un color diferente sale un ERROR y vuelve a preguntar.
-Si se introduce números o caracteres raros también sale ERROR y vuelve a preguntar
-Si se presiona Ctrl+C se cierra el programa drectamente.

