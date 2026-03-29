# Método strip string: Remueve los caracteres puestos en los paréntesis y retornando la
# variable ya modificada.

texto = "     Ejemplo para usar el strip."
cutleft = texto.lstrip()
print(cutleft)

link = "www.youtube.com/"
cutlink = link.strip("w./")
print(cutlink)