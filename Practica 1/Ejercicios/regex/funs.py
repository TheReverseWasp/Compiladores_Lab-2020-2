import re

def ej1(text):
    i = "([0-9]|([1-9][0-9])|([1|2][0-9][0-9]))"
    p = "\."
    r = re.compile(i + p + i + p + i + p + i)
    if r.match(text):
        return "SI ES UNA IP"
    else:
        return "NO ES UNA IP"

def ej2(text):
    i = "([A-Z|a-z|_])"
    e = "([A-Z|a-z|_|0-9]*)$"
    r = re.compile(i + e)
    if r.match(text):
        return "SI ES UNA VARIABLE"
    else:
        return "NO ES UNA VARIABLE"

def pulir_solicitud(l):
    t = []
    for i in l:
        t.append(i[1])
    return t

def ej3(text):
    solicitud1 = "([m|M]e gustaria pedirle )([a-z|A-Z|0-9|\$| ]*)([\.|,])"
    solicitud2 = "([d|D]esearia encargarle )([a-z|A-Z|0-9|\$| ]*)([\.|,])"
    solicitud3 = "([q|Q]uisiera pedirle )([a-z|A-Z|0-9|\$| ]*)([\.|,])"
    l1 = re.findall(solicitud1, text)
    l2 = re.findall(solicitud2, text)
    l3 = re.findall(solicitud3, text)
    l1 = pulir_solicitud(l1)
    l2 = pulir_solicitud(l2)
    l3 = pulir_solicitud(l3)
    l = l1 + l2 + l3
    return "NO HAY UNA SOLICITUD" if len(l) == 0 else "SOLICITUDES: " + str(l)
