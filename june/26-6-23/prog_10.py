import re

st = "This is the new string in which you can do Anything."

x = re.search("new", st)
print(x.start())
print(x.end())
