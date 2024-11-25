'''Escribir un programa que cree un diccionario de traducción español-inglés. El usuario introducirá las palabras en español e inglés separadas por dos puntos, y cada par <palabra>:<traducción> separados por comas, hasta que el usuario introduzca la palabra “terminar”. El programa debe crear un diccionario con las palabras y sus traducciones. Después pedirá una frase en español y utilizará el diccionario para traducirla palabra a palabra. Si una palabra no está en el diccionario debe dejarla sin traducir.
'''
diccionario = {}
print("Introduce palabras'(español:inglés'), utiliza comas para separar.")
print("Escribe 'stop' para dejar de meter palabras.")

while True:
    entrada = input("Palabras: ")
    if entrada == "stop":
        print("Fin de diccionario.")
        break
    pares = entrada.split(",")
    for par in pares:
        if ":" in par:
            esp, ing = par.split(":")
            diccionario[esp.strip()] = ing.strip()
print("Diccionario:")
for esp, ing in diccionario.items():
    print(f"{esp}: {ing}")
frase = input("Escribe frase en español: ")

traduccion = []
for palabra in frase.split():
    traduccion.append(diccionario.get(palabra, palabra))

print("Traducción:")
print(" ".join(traduccion))
