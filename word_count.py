with open("lorem_ipsum.txt","r") as file: 
    texto = file.read()

# Contar caracteres distintos
caracteres_distintos = set(texto)
cant_caracteres_distintos = len(caracteres_distintos)

# Contar palabras distintas
palabras = texto.split()
palabras_distintas = set(palabras)
cant_palabras_distintas = len(palabras_distintas)

print(f"El número de caracteres distintos es: {cant_caracteres_distintos}")
print(f"El número de palabras distintas es: {cant_palabras_distintas}")