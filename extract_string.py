import re
s = "name<laishram rahul>.  "
m = re.findall("<(.*?)>", s)
print(m[0])