# De forma teórica, realice una expresión que valide palabras que contengan dos b's seguidas
# o dos a's seguidas ejemplo abbaaa, bbaaa; aba no cumple.

import re

txt = "haabbz"
exp = ".*(a{2}|b{2}).*(b{2}|a{2}).*"

if re.fullmatch(exp, txt):
  print("Aceptado")
else:
  print("No aceptado")