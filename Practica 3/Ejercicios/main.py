from AL import *

def main():
    while True:
        linea = input()
        try:
            for i in analizadorLexico(linea):
                print("Token: { tipo:", i.tipo, ", palabra:", i.palabra, ", idx:", i.inicio, "}")
        except:
            print("Error encontrado fin del Analizador Lexico")
            return False

if __name__ == "__main__":
    main()
