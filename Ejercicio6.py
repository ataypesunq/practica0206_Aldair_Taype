'''Escribir un programa que permita gestionar la base de datos de alumnado de un classroom. Los alumnos y alumnas se guardarán en una lista que almacena un diccionario para cada alumno/a en el que la clave de cada alumno/a será su NIF, y el valor será otro diccionario con los datos del alumno/a (nombre, apellidos, teléfono, correo, aprobado), donde aprobado tendrá el valor True si ha aprobado el módulo. El programa debe preguntar al usuario por una opción del siguiente menú: (1) Añadir alumno/a, (2) Eliminar alumno/a, (3) Mostrar alumno/a, (4) Listar todo el alumnado, (5) Listar alumnado aprobado, (6) Terminar. En función de la opción elegida el programa tendrá que hacer lo siguiente:
Preguntar los datos del alumno/a, crear un diccionario con los datos y añadirlo a la base de datos.
Preguntar por el NIF del alumno/a y eliminar sus datos de la base de datos.
Preguntar por el NIF del alumno/a y mostrar sus datos.
Mostrar lista de todo el alumnado de la base de datos con su NIF y nombre.
Mostrar la lista del alumnado aprobado de la base de datos con su NIF y nombre.
Terminar el programa.
'''
base_datos = []

def mostrar_menu():
    print("\nMenú de opciones:")
    print("1. Añadir alumno/a")
    print("2. Eliminar alumno/a")
    print("3. Mostrar alumno/a")
    print("4. Listar todo el alumnado")
    print("5. Listar alumnado aprobado")
    print("6. Terminar")

while True:
    mostrar_menu()
    opcion = input("\nSelecciona una opción (1-6): ")
    
    if opcion == "1":
        nif = input("Escribe el NIF del alumno/a: ")
        nombre = input("Escribe el nombre del alumno/a: ")
        apellidos = input("Escribe los apellidos del alumno/a: ")
        telefono = input("Escribe el teléfono del alumno/a: ")
        correo = input("Escribe el correo del alumno/a: ")
        aprobado = input("Aprobado? (sí/no): ").lower() == "sí"
        