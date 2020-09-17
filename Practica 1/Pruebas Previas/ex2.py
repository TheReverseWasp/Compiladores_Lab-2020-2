import re

regstr = '[a-z]+'
text = "abc cde 777ghi jkl999mno"

groups = re.findall(regstr, text)

print(str(groups))
