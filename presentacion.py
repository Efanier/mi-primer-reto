nombre = "Luis EFanier Sánchez Echavarria"
edad = 31
lenguaje = "Python"
print(f"Hola, mi nombre es {nombre}, tengo {edad} años y estoy aprendiendo {lenguaje}. Hola estoy modificando")

def comida_favorita():
    comida = "Chicharron"
    print(f"Mi comida favorita es {comida}")

comida_favorita()
color = input("¿Cual es tu color favorito? ")
print(f"Tu color favorito es {color}")

usuario = input("Escribe tu usuario: ")
contaseña = input("Escribe una contaseña: ")
confirmar_contraseña = input("Escribe una contaseña: ")
validacion = contaseña == confirmar_contraseña