#Codigo por Ricardo Lazo Vásquez - ricardo.lazo@ucsp.edu.pe
#correspondiente al segundo problema de la practica 0
def main():
    s = input().split(" ")
    spc = {"reir": "riendo", "salir": "saliendo", "abatir": "abatiendo"}
    if s[0] in spc:
        ch = spc[s[0]]
    elif s[0][-2:] == "ar":
        ch = s[0][:-2] + "ando"
    elif s[0][-2:] == "er" or s[0][-2:] == "ir":
        if s[0][-3] == "a" or s[0][-3] == "u":
            ch = s[0][:-2] + "yendo"
        elif s[0][-2:] == "er":
            ch = s[0][:-2] + "iendo"
        elif s[0][-2:] == "ir":
            ch = s[0][:-2] + "endo"
    if ch == s[1]:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()
