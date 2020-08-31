#Codigo por Ricardo Lazo Vásquez - ricardo.lazo@ucsp.edu.pe
#correspondiente al primer problema de la practica 0

def fun(s):
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
                    return "NO"
                    return 0
            else:
                l.append(i)
    return "YES" if len(l) == 0 else return "NO"

def main():
    s = input()
    print(fun(s))

if __name__ == "__main__":
    main()
