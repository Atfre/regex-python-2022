# Que valide un email de dominio aol.com, yahoo.com, latinmail.com ejemplo repruebo@aol.com.

import re

txt = "repruebo@yahoo.com"
exp = "[a-z0-9]+(@aol|@yahoo|@latinmail).com"

if re.fullmatch(exp, txt):
  print("Aceptado")
else:
  print("No aceptado")