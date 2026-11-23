#Ejercicio 1. Variables y tipos
#   Crea tres variables:
#   nombre, con tu nombre.
#   edad, con tu edad.
#   altura, con tu altura en metros.
#Muestra el contenido de las tres variables y, después, muestra el tipo de cada una utilizando type().
nombre = "hugo"
edad = 20
altura = 1,70
print(nombre, edad, altura)
print(type(nombre))
print(type(edad))
print(type(altura))

#Ejercicio 2. Cadenas
#Partiendo de:
#frase = "Python es divertido"
#haz que el programa:
#   Muestre la frase en minúsculas.
#   Muestre su longitud.
#   Compruebe si contiene la palabra "python" sin distinguir mayúsculas y minúsculas.
#   Muestre la frase al revés.
frase = "Python es divertido"
print(frase.lower())
print(len(frase))
print("python" in frase.lower())
print(frase[::-1])

#Ejercicio 3. Booleanos
#Crea una variable:
#es_administrador = False
#Utiliza un if y un else para mostrar:
#Acceso de administrador
#si su valor es verdadero, y:
#Acceso de usuario
#si es falso.
#Después cambia su valor a True y observa el resultado.
es_administrador = True
if es_administrador:
    print("Acceso de administrador")
else:
    print("Acceso de usuario")

#Ejercicio 4. Conversión de tipos
#Pide al usuario el precio de un producto y una cantidad:
#Precio: 
#Cantidad:
#Convierte los valores a los tipos adecuados y calcula el importe total:
#importe = precio * cantidad
#Muestra finalmente el resultado.
precio = int(input("Precio: "))
cantidad = int(input("Cantidad: "))
print("El precio total es de", precio * cantidad, "€")

#Ejercicio 5. Pequeño reto
#Pide al usuario su nombre y su año de nacimiento. Calcula aproximadamente su edad suponiendo que estamos en 2026 y muestra un mensaje similar a:
#Ana, tienes aproximadamente 20 años.
nombre = input("Nombre: ")
year = int(input("Año de nacimiento: "))
edad = 2026 - year
print(nombre, "tienes aproximadamente", edad, "años")