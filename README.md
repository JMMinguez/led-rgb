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



