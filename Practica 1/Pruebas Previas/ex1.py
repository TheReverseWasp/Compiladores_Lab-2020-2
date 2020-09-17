import re

p = re.compile('[0-9]+$')

if p.match("1111"):
    print("SI ES UN NUMERO")
else:
    print("NO ES UN NUMERO")
