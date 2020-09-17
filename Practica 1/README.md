## Consideraciones Previas
- Las pruebas unitarias solo se realizaron para regex
- Para flex pueden cambiar el archivo prueba.txt como quieran la salida se mostrara en el archivo salida.txt
	- para compilar ejecutar:
		-      flex f.l
		-      gcc lex.yy.c -L/lib -lfl
	- pero esto no es necesario ya que cuentan con el a.out, para esto solo deberian ejecutar
    	-      ./a.out < prueba.txt > salida.txt
y la salida se mostrara en el archivo salida.txt


## Pruebas Unitarias de regex (Python)
- Los scripts de pruevas estan en la carpeta "Pruebas Unitarias"
- Para probar si los scripts estan bien en las pruebas propuestas ejecutar "python3 tej1.py" para el ejercicio 1, "python3 tej2.py" para el ejercicio 2 y de la misma manera para el ejercicio 3.
- Para ejecutar pruebas personalizadas (las ejecutadas por el profesor) acceder a la carpeta "Ejercicios/regex" y ejecutar:
	-    python3 ej + "# de ejercicio" + .py

Link del github (repositorio) donde se encuentran todos los datos del alumno: https://github.com/TheReverseWasp/Compiladores_Lab-2020-2
