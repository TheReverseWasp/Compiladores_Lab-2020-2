#Codigo por Ricardo Lazo Vásquez - ricardo.lazo@ucsp.edu.pe
#correspondiente al tercer problema de la practica 0
def search_for(segment, kchar):
    acum = 0
    for i in segment:
        if i == kchar:
            return acum + 1
        acum += 1
    return -1

def fun(str):
    lstr = str.split("\n")
    tc = int(lstr[0])
    answer = ""
    for i in range(1, tc + 1):
        answer += "Problem #" + str(i) + "\n"
        p = {"m": 0.001, "k": 1000, "M": 1000000}
        d = {"I=": False, "U=": False, "P=": False}
        dc ={"I=": "A", "U=": "V", "P=": "W"}
        s = lstr[i]
        while len(s) > 2:
            if s[:2] in d:
                temp = search_for(s[2:], dc[s[:2]])
                d[s[:2]] = s[2: 2 + temp - 1]
                s = s[2 + temp:]
            else:
                s = s[1:]
        for i in s:
            if i[:2] in d:
                d[i[:2]] = i[2:]
                while d[i[:2]][-1] != dc[i[:2]][0]:
                    d[i[:2]] = d[i[:2]][:-1]
                d[i[:2]] = d[i[:2]][:-1]
        for k, v in d.items():
            if v != False:
                if v[-1] in p:
                    d[k] = float(v[:-1]) * p[v[-1]]
                else:
                    d[k] = float(v)
        for k, v in d.items():
            if v == False:
                if k == "I=":
                    answer += k + str('{0:.2f}'.format(d["P="] / d["U="])) + "A" + "\n"
                elif k == "P=":
                    answer += k + str('{0:.2f}'.format(d["I="] * d["U="])) + "W" + "\n"
                elif k == "U=":
                    answer += k + str('{0:.2f}'.format(d["P="] / d["I="])) + "V" + "\n"
        answer += "\n"
    return answer

def main():
    nls = input()
    nli = int(nls)
    for i in range(nli):
        s = input()
        nls += "\n" + s
    nls += "\n"
    print(fun(str))

if __name__ == "__main__":
    main()
