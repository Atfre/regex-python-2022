# Que acepte una coordenada con latitud y longitud.

import re

txt = "36.738851,119.801764"
exp = "([0-9]+\.[0-9]*)\,([0-9]+\.[0-9]*)"

if re.fullmatch(exp, txt):
  print("Aceptado")
else:
  print("No aceptado")