#bucle for basico
for i in range(5):
    print(i)
#range(5) genera los valores del 0 al 4, por lo que el print seria un numero por linea

#Se puede indicar el inicio y el final
for i in range(10, 20):
    print(f"{i} ", end=" ") #El valor end es para que salga en la misma linea

#Acumuladores
suma = 0
ini = int(input("inicio: "))
fin = int(input("fin: "))

for i in range(ini, fin + 1): #Con el +1 si saldria el numero del final del rango
    print(i)
    suma = suma + i
print("\nSuma:", suma) #Acumula el resultado de i (que es la suma de todo el range)

#Bucle while
numero = int(input("Introduce un número (0 para terminar): "))
while numero != 0:
    print("Has introducido:", numero)
    numero = int(input("Introduce otro número (0 para terminar): "))

print("Fin del programa")
#La condicion se cumple siempre que el numero no sea cero (!= 0)
#Es muy importante volver a pedir otra condicion (numero en este caso) para que el bucle no se repita infinitamente

#while true y break
#Esto hace algo muy parecido a lo anterior
while True:
    numero = int(input("Introduce un número (0 para terminar): "))
    if numero == 0:
        break
    print("Has introducido:", numero)
print("Fin del programa")

#Es lo mismo:
#while numero != 0:
 #   que
#while True:
#    ...
#    if numero == 0:
#        break

#Recorrer una cadena de texto
#Lo que hace es mostrar los caracteres de la variable
nombre = "www.aulas.local"

for x in nombre:
    print(x)

#Recorrer la cadena usando indices
#Se pueden recorrer las posiciones de cada caracter
for i in range(len(nombre)):
    print(f"{i}: {nombre[i]}")
#Osea, seria algo como 
#0: w 
#1: w
#...
