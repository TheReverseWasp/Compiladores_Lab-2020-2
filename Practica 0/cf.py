def ej1(s):
    d1 = {"{": 0, "}":1, "[": 2, "]": 3, "(": 4, ")": 5}
    d2 = {0: "{", 1: "}", 2: "[", 3: "]", 4: "(", 5: ")"}
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
    return "YES" if len(l) == 0 else "NO"

def ej2(s):
    s = s.split(" ")
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
        return "YES"
    else:
        return "NO"

def search_for(segment, kchar):
    acum = 0
    for i in segment:
        if i == kchar:
            return acum + 1
        acum += 1
    return -1

def ej3(s):
    lstr = s.split("\n")
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
                    answer += k + '{0:.2f}'.format(d["P="] / d["U="]) + "A" + "\n"
                elif k == "P=":
                    answer += k + '{0:.2f}'.format(d["I="] * d["U="]) + "W" + "\n"
                elif k == "U=":
                    answer += k + '{0:.2f}'.format(d["P="] / d["I="]) + "V" + "\n"
        answer += "\n"
    return answer
