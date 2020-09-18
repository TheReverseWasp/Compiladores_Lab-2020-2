## Práctica 3
Por: Ricardo Manuel Lazo Vásquez

Como se explicó en clases, el analizador léxico contribuye de alguna manera a futuros pasos pero no en todos los casos.

En algunos casos el analizador no reconoce estos errores

123abv -> que debería reconocerlo como un error se reconoce como un token numero seguido de un token variable.

Para ejecutar en esta carpeta acceder a la carpeta ./Ejercicios y ejecutar: python3 main.py

Ejecutará un script que empezara a recibir las lineas de ejemplo, pueden ingresar las cadenas que quieran teniendo en cuenta que solo reconoce números enteros, variables y operadores(+, -, *, /, =), también reconoce espacios.

En caso de ingresar una cadena errónea el programa terminará inmediatamente.

