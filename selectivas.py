#Selectiva if
edad = int(input("Edad: "))
print(type(edad))


if edad >= 18: #Su resultado es como un True o False
    print("Adulto") #La identacion es importante, este print esta dentro del if (TIene 18 o mas años)
else #Es el resultado si no se cumple la condicion if
    print("Menor de edad") #Tiene menos de 18 años

print("Fin del if") #Este no esta dentro del if

#and y or
edad = int(input("Edad: "))
print(type(edad))
saldo = int(input("Saldo: "))
print(type(saldo))

if (edad >= 18 and saldo > 0) or (saldo > 10000):
    print("Apto")
else 
    print("No apto")

print("Fin and y or")

#Selectivas anidadas
a = int(input("valor de a: "))
b = 200

if b > a
    print("b es mayor que a") #Primera condicion
else
    if b < a 
        print("a es menor que b") #Segunda condicion
    else
        print("Ambos numeros son iguales") #Tercera condicion
#Si la primera y segunda condicion no se cumplen, solo queda la tercera
#Tambien se puede hacer lo mismo de forma mas simple con elif
if b > a
    print("b es mayor que a") #Primera condicion
elif
    print("a es menor que b") #Segunda condicion
else
    print("Ambos numeros son iguales") #Tercera condicion
#Basicamente es como decir "si no es esto, es lo otro, si tampoco es, es lo otro"
print("fin anidadas")

#Selector multiple
opcion = int(input("Escoge una opcion: "))
match opcion:
    case 0: #Has escrito 0
        print("Has elegido opcion 0")
    case 1: #Has escrito 1
        print("Has elegido opcion 1")
    case _: #Has escrito otra cosa
        print("Valor por defecto")
