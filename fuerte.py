# Ejemplo de tipado fuerte en Python

x =  10   # entero (int)
y = "5"  # cadena (str)

# Esto generara un error:

#print(x + y)

# Python no convierte la cadena "5" en numero automaticamente

# para convertir la candena "5" en numero, se puede hacer lo siguiente:

print(x + int(y))