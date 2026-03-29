# Que acepte un color rgba ejemplo:rgba(230,144,133,0.5).

import re

txt = "rgba(255,200,150,0.25)"
exp = "rgba\((25[0-5]|2[0-4][0-9]|1?[0-9]{1,2}),\s?(25[0-5]|2[0-4][0-9]|1?[0-9]{1,2}),\s?(25[0-5]|2[0-4][0-9]|1?[0-9]{1,2}),\s?(0(\.\d+)?|1(\.0+)?)\)"

if re.fullmatch(exp, txt):
  print("Aceptado")
else:
  print("No aceptado")