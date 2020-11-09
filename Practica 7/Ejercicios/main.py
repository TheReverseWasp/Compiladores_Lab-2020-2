from TASFinal import *

def main():
    gram = Gram_Prac4()
    mi_interprete = Interprete(gram, analizadorLexico)
    mi_interprete.crear_tabla()
    print("----------------Interprete Dinamico--------------------")
    mi_interprete.imprimir_tas()
    print("----------------Fin Interprete Dinamico--------------------")
    while True:
        print("Ingrese una linea")
        linea = input()
        expresion = mi_interprete.verificar_correctitud(linea)
        if not expresion:
            print("Gramatica Incorrecta")
        else:
            print("Gramatica Correcta")   
            expresion.imprimirExpresionInterpretada(0)

if __name__ == "__main__":
    main()
