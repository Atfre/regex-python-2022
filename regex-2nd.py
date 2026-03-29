# De forma teórica, realice una expresión que valide palabras que inician
# y terminan con a y contienen al menos una b.

import re

txt = "acdba"
exp = "(a).*(b).*(a)"

if re.fullmatch(exp, txt):
  print("Aceptado")
else:
  print("No aceptado")