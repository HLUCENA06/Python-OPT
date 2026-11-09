#VARIABLES 
numero = 1 #No es una cadena de texto
texto = "Hola a todos" #Si es una cadena de texto
#Las variables no pueden llamarse iguales, sin embargo, si una variable es minuscula y otra es mayuscula si sirve
EJEMP = "MAYUSCULA"
ejemp = "minuscula"

#Se pueden hacer operaciones
suma1 = 2
suma2 = 3
print(suma1 + suma2)
#El resultado de la operacion tambien se puede guardar en una variable
resultado = suma1 + suma2
print(resultado)

#CADENAS DE TEXTO
#Se pueden recibir varios valores y concatenarlos separando con comas
print("El resultado de", suma1, "+", suma2, "Es igual a", resultado)
#Tambien se puede hacer de esta forma
print(f"El resultado de {suma1} + {suma2} es igual a {resultado:.1f}")
#:.1f hace que el dato numerico se muestre con un decimal (en caso de tener mas de uno, solo mostraria 1)

#Consultar el tipo de un dato
print(type(numero))
#Tendria que salir Int
#pero si yo ahora cambio numero por otra cosa a continuacion
numero = "Hola"
print(type(numero))
#El tipo cambia a Str

#Se pueden modificar las cadenas de texto, por ejemplo para que un texto salga en minuscula o mayuscula
print("HOLA A TODOS".lower())
print(EJEMP.lower())
print(ejemp.upper())
#Se puede modificcar la variable para que a partir de aqui sea mayuscula
ejemp = ejemp.upper()
print(ejemp)
#Tambien esta el modificador replace para remplazar palabras
saludo = "Hola amigos como estan"
print(saludo.replace("amigos", "nigas"))

#Se puede obtener la longitud de un caracter o un caracter exacto, siendo el primer caracter 0
print(saludo[0])
print(saludo[1])
print(len(saludo)) #Con esto se obtiene la longitud
l_saludo = len(saludo)
print(l_saludo)
#Tambien puedo extrar una parte de un texto
print(saludo[:6]) #Empieza a mostrar las letras desde el inicio
print(saludo[1:]) #Se va comiendo las letras desde el inicio
print(saludo[::2]) #Con esto recorre la cadena de dos en dos, osea, solo da los caracteres pares
print(saludo[:-3]) #Empieza por el final
print(saludo[-3:])

#Buscar texto con in y not in
busca = "n-word"
frase1 = "amo la nword"
if busca not in frase1:
    print(f"{busca} si esta en la frase")
else:
    print(f"{busca} NO esta en la frase")

#Bucles
nombre = "netanyahu"
for x in nombre:
    print(x) #Este bucle da todos los caracteres de la variable

for i in range(len(nombre)):
    print(f"{i}: {nombre[i]}")

#Variables booleanas
autorizado = False    # el otro valor posible True
print( type(autorizado)  )

if autorizado: #Su valor es lo establecido en la variable
    print("Puede pasar")
    print("Resto del bloque positivo")
else:
    print("No puede pasar")
    print("Resto del bloque negativo")

#Conversion de tipos
saldo = input("Saldo: ")
saldo2 = input("Saldo2: ")
print("Mi saldo es de: ", saldo)
print(saldo + saldo2) #De esta forma, como los input estan como caracteres, si escribo numeros no se van a sumar, solo se van a juntar, para arreglar eso hay que cambiar el tipo 
saldo = float(saldo)
saldo2 = float(saldo2)
print(saldo + saldo2)
#Si sabemos desde el principio que necesitamos un número, también podemos convertir directamente el resultado de input
saldo3 = float(input("Saldo: "))
print("Mi saldo REAL es de. ", saldo3)
#Si un input que esta dentro de un float se deja en blanco o se escriben letras, da error