#Codigo por Ricardo Lazo Vásquez - ricardo.lazo@ucsp.edu.pe
#correspondiente al tercer problema de la practica 0
from cf import *

def main():
    nls = input()
    nli = int(nls)
    for i in range(nli):
        s = input()
        nls += "\n" + s
    nls += "\n"
    print(ej3(nls))

if __name__ == "__main__":
    main()
