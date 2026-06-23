import os

name = os.getenv("Nombre")
edad = int(os.getenv('Edad'))

if edad >= 18:
    print(f"{name} es mayor de edad")
else:
    print(f"{name} es menor de edad")