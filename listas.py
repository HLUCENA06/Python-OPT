#Las listas permiten almacenar varios valores en una misma variable
puertos = [22, 80, 443, 8080] #Esto es una lista

#Puedo acceder a los elementos de una lista por su posicion
print(puertos[0]) #0 es el primero, sera 22
print(puertos[1]) #1 es el segundo, sera el 80

#Se puede obtener el numero de elementos de una lista
print ("Nº elementos de la lista: ", len(puertos))

#Obtener parte de una lista
frutas = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print("frutas", frutas) #Muestra todas las frutas
print("frutas[1:4]", frutas[1:4]) #Empieza por el segundo (1) y termina por el quinto (4)
print(frutas[-1]) #Acceder al ultimo elemento

#Se pueden modificar los elementos de las listas
frutas[0] = "watermelon" #apple pasa a ser watermelon
print(frutas)

#Comprobar si la lista esta vacia
lista = [1,2]
if len(lista) != 0:
    print("La lista tiene elementos")
else:
    print("Lista vacia")

#Recorrer una lista
lista_IP = ["192.168.1.1", "10.10.10.10", "172.16.100.100", "195.172.1.1"]
for x in lista_IP:
    print("IP: ", x)
#O con las posiciones
for x in range(len(lista_IP)):
    print(f"IP[{x}]: {lista_IP[x]}")

#Buscar elementos en una lista
ip = input("IP a buscar: ")
if ip in lista_IP:
    print(f"Yes, {ip} is in {lista_IP}") 
else:
    print(f"No, {ip} is not in {lista_IP}") 

#Tambien se puede hacer con try/except
try:
    pos = lista_IP.index(ip)
    print(f"{ip} está en la posición {pos}")
except ValueError:
    print(f"{ip} NO está en {lista_IP}")

#Ordenar listas
edades = [19, 17, 23, 56, 48, 100, 31]
edades.sort() #Ordena de menor a mayor
print("edades tras edades.sort():", edades)
edades.reverse() #Invierte el orden de la lista
print("edades tras edades.reverse():", edades)
print("edades:", edades)
edades.append(20) #Añadir un valor al final
print("edades tras edades.append(20):", edades)
edades.insert(1, 44) #Insertar un valor (44) en una posicion (1)
print("edades tras edades.insert(1,44):", edades)
eliminado = edades.pop() #Eliminar un elemento. por defecto elimina el ultimo de la lista, despues lo almacena en el valor eliminado. Se puede indicar su posicion entre parentesis
print("edades tras eliminado = edades.pop()", edades)
print("eliminado:", eliminado )
edades.clear() #Vaciar la lista
print("edades tras clear", edades)

#Convertir string en lista (split)
users = "ana:luis:alfredo"
lista = users.split(":")
print("users:", users)
print("type(users)", type(users))
print("lista: ", lista)
print("type(lista)", type(lista))

#Leer varios valores y hacer la media
lectura = input("Notas separadas por el caracter ';': " )
print(lectura, type(lectura)) # es un string
notas = lectura.split(";") # es una lista
print(notas, type(notas))

suma = 0 # Almacena la suma de las notas
for x in notas:
    suma = suma + float(x)
media = suma/len(notas)
print("Suma: ", suma)
print(f"Media: {media:.2f}")

#Conversion de una lista de numeros a una lista string
edades = ["14", "21", "17", "33", "45"]
print("type(edades[0]):", type(edades[0]))
# comprensión de listas
edades =  [int(x) for x in edades]
print("type(edades[0]):", type(edades[0]))