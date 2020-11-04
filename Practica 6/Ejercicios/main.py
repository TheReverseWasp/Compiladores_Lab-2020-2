from TAS import *
from TAS2 import *

def main():
    gram = Gram_Prac4()
    TAS_estatico = TAS_Static_P6(gram, analizadorLexico)
    TAS_dinamico = TAS_Dynamic_P6(gram, analizadorLexico)
    TAS_dinamico.crear_tabla()
    print("\tComparacion de TAS")
    print("----------------TAS Estatico--------------------")
    TAS_estatico.imprimir_TAS()
    print("----------------TAS Dinamico--------------------")
    TAS_dinamico.imprimir_TAS()
    print("------------------------------------")
    while True:
        print("Ingrese una linea")
        linea = input()
        TAS_dinamico.check_if_correct(linea)

if __name__ == "__main__":
    main()
