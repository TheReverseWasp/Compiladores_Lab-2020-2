#Codigo por Ricardo Lazo Vásquez - ricardo.lazo@ucsp.edu.pe
#correspondiente al primer problema de la practica 0
def main():
    d1 = {"{": 0, "}":1, "[": 2, "]": 3, "(": 4, ")": 5}
    d2 = {0: "{", 1: "}", 2: "[", 3: "]", 4: "(", 5: ")"}
    s = input()
    l = []
    for i in s:
        if i in d1:
            if d1[i] % 2 == 1:
                if len(l) > 0 and l[-1] == d2[d1[i] - 1]:
                    l.pop()
                else:
                    print("NO")
                    return 0
            else:
                l.append(i)
    print("YES") if len(l) == 0 else print("NO")

if __name__ == "__main__":
    main()
