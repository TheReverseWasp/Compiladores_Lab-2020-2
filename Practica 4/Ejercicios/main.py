from TAS import *

def main():
    gram = Gram_Prac4()
    TAS = TAS_Prac4(gram, analizadorLexico)
    while True:
        print("Ingrese su linea de codigo")
        line = input()
        TAS.check_if_correct(line)

if __name__ == "__main__":
    main()
