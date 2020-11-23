from Interprete import *

def main():
    gram = Gram()
    TAS = TASMaestra(gram, analizadorLexico)
    TAS.crearTabla()
    TAS.imprimirTAS()
    interprete = Interprete(TAS)
    print("------------------------Analizador de Lineas---------------------")
    while True:
        linea = input("Ingrese la linea a analizar:\n")
        expr = interprete.verificarCorrectitud(linea, "E")
        expr.imprimirExpresionInterpretada()

if __name__ == "__main__":
    main()
