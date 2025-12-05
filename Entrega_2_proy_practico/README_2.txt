Santiago Barrientos, Juan Esteban Rayo y Manuel Gutiérrez.
=============================================================
          JUEGOS: Snake y Tetris (Configuraciones .brik)
=============================================================

Este documento resume las configuraciones de las implementaciones de Snake y Tetris, 
basadas en los archivos 'snake.brik' y 'tetris.brik'.

Forma de ejecución: 
La carpeta ya contiene los árboles sintácticos. Por tanto, para la ejecución
del juego, basta con ir a la carpeta donde está todo ubicado y ejecutar el
 comando: Python runtime.py

-------------------------------------------------------------
                        TETRIS 
-------------------------------------------------------------

Algunas características como colores no se añadieron dada la simplesa 
del juego, sin embargo, es posible implementarlas si se usa una interfáz
gráfica y no hay limitaciones de espacio.

###  PARÁMETROS GENERALES
* Nombre del Juego: 'Tetris' 

* Versión: 1.0 

* [dimensiones_tablero] : {
  ancho: 10
  alto: 20
}

* Velocidad Inicial de Caída: 1.0 

###  REGLAS CLAVE
* Puntuación por Líneas: La puntuación base es 100. Se usa un multiplicador por la cantidad de líneas completadas a la vez: [1, 3, 5, 8].
* Aumento de Velocidad: La velocidad aumenta con los niveles, con un aumento por cada 1000 puntos, usando un multiplicador de 1.2
* Regla de Finalización: El juego termina cuando una pieza alcanza el tope del tablero y no puede ser colocada.

###  PIEZAS 
El juego incluye las piezas clásicas (I, O, T, L, J, S, Z).


###  CONTROLES
* Mover Izquierda/Derecha: 'a' / 'd' 
* Acelerar Caída (Soft Drop): 's' 
* Evitar Caída (Rotar / Hold?): 'w' 
* Pausar / Reiniciar: 'p' / 'r' 
* Salir: 'esc'

-------------------------------------------------------------
                       SNAKE (SERPIENTE) 
-------------------------------------------------------------
Algunas reglas u obstáculos no se incluyeron por la simplesa 
del juego, sin embargo, es posible añadirlo si se usa una interfáz
gráfica y no hay limitaciones de espacio.

###  PARÁMETROS GENERALES
* Nombre del Juego: 'snake' 
* Versión: 1.0 
* [dimensiones_tablero] : {
  ancho: 10
  alto: 20
}
* Velocidad Inicial: 2.5 celdas por segundo 

###  REGLAS Y COMIDA
* Regla de Comida Básica: Al comer, se activa el evento 'serpiente_come', la acción es 'aumentar_longitud', y otorga 10 puntos por comida.
* Comida  (verde):Tipo 'manzana_regular', otorga 10 puntos.
* Comida Especial (amarillo): Tipo 'manzana_dorada', otorga 50 puntos extra y dura 8 segundos en el tablero.
* Comida Nociva (negro): Tipo 'manzana_negra', resta 50 puntos extra  y dura 10 segundos.

### OBSTÁCULOS Y VELOCIDAD (Idea para implementar en caso que se pueda usar una interfaz gráfica)
* Obstáculos: Están activos y se generan de forma aleatoria , con una cantidad máxima de 10.
* Aumento de Velocidad: La velocidad aumenta cada 100 puntos , usando un multiplicador de 1.1
* Colisiones: Se considera fin de juego el "choque_pared" o "choque_cola". Las colisiones contra la pared y contra la cola están activadas.


### CONTROLES
* Mover Arriba/Abajo/Izquierda/Derecha: 'w' / 's' / 'a' / 'd' 
* Pausar / Reiniciar / Salir: 'p' / 'r'/'esc'

