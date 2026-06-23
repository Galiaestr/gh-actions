import os

name = os.getenv('NAME')
age = int(os.getenv('EDAD'))

print("Hola" + name)

if age >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")