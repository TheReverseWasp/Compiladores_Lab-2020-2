import re
import copy as cp

class Token:
    def __init__(self, p, i, f, t):
        self.palabra = p
        self.inicio = i
        self.fin = f
        self.tipo = t

def reconocerToken(r, linea, idx, tipo):
    f = cp.copy(idx)
    flag = False
    while r.match(linea[idx:f + 1]) and f < len(linea):
        f += 1
        flag = True
    if flag:
        t = Token(linea[idx:f], idx, f, tipo)
        return t
    return False

def reconocerNumero(linea, idx):
    n = "[0-9]*$"
    r = re.compile(n)
    return reconocerToken(r, linea, idx, "Numero")

def reconocerVariable(linea, idx):
    v = "[a-z|A-Z]([a-z|A-Z|0-9]*)$"
    r = re.compile(v)
    return reconocerToken(r, linea, idx, "Variable")

def reconocerOperador(linea, idx):
    o = "[\+|\-|\*|/|\=]$"
    r = re.compile(o)
    return reconocerToken(r, linea, idx, "Operador")

def getToken(linea, idx):
    funs = [reconocerNumero, reconocerOperador, reconocerVariable]
    for i in funs:
        t = i(linea, idx)
        if t != False:
            return t
    return False

def analizadorLexico(linea):
    idx = 0
    tokens = []
    while idx < len(linea):
        t = getToken(linea, idx)
        try:
            idx = t.fin
        except:
            print("Error en la posición", idx, "Token invalido")
            return False
        tokens.append(cp.copy(t))
    return tokens
