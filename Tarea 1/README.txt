
2019-1
Rodrigo Cayazaya 201773538-4
Jean-Franco Z�rate 201773524-4
Axel Reyes 201773502-3

Los requerimientos de esta tarea se encuentran en Tarea_1.pdf y sus archivos son Nintendo.csv y Sansanoplay.csv. Se utiliz� el lenguaje Python para crear las consultas.

Requisitos:
	- Usar Oracle 11g
	- Usar Windows 10
	
En la linea 234 de Crear.py y linea 382 de Consultas.py reemplazar los corchetes por los valores correspondientes o usar los datos de su BD correctamente:
	Driver={Oracle in XE};
	DBQ=[DBQ];
	Uid=[Usuario (SYSTEM)];
	Pwd=[Contrase�a de su BD]

En caso de fallos usar el driver como:
	Driver={Oracle en OraDb11g_home1}


En el .zip vienen dos archivos, uno llamado "Crear.py" que es para la creacion de las tablas e inserci�n de datos correspondientes.
Este archivo s�lo posee funciones que son llamadas en el programa principal. Hay que tener en cuenta de que las funciones de borrado vienen comentadas, por lo que si desea correr nuevamente el c�digo debe descomentar las funciones de borrado para que al inicio del programa se borren las ya existentes y se creen nuevamente.

El otro archivo llamado "Consultas.py" es para realizar las consultas.

Para la ejecuci�n correcta de ambos c�digos debe utilizar los datos correspondientes a su base de datos y a su versi�n de Oracle.
