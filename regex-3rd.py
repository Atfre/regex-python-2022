# Que acepte un password de entre 8 y 16 caracteres mayúsculas o minúsculas y
# que contenga al menos un símbolo y un número.

import re

txt = "pAsSwOrD123!"
exp = "[A-Za-z0-9@!#$]{8,16}"

if re.fullmatch(exp, txt):
  print("Aceptado")
else:
  print("No aceptado")