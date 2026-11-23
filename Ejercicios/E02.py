# Ejercicio 1. Mayor de edad
# Pide al usuario su edad.
# Si tiene 18 años o más, muestra:
# Es mayor de edad
# Si no, muestra:
# Es menor de edad
edad = int(input("Dime tu edad: "))
if edad >= 18:
    print("Eres mayor de edad, tienes", edad, "años")
else:
    print("Eres menor de edad, tienes", edad, "años")

# Ejercicio 2. Número positivo, negativo o cero
# Pide al usuario un número entero y determina si es:
# positivo;
# negativo;
# cero.
# Utiliza if, elif y else.
numero = int(input("Introduce un numero: "))
if numero > 0:
    print(numero, "Es un numero positivo")
elif numero < 0:
    print(numero, "Es un numero negativo")
else:
    print("El numero es 0")

# Ejercicio 3. Acceso al sistema
# Pide al usuario:
# su edad;
# si dispone de saldo.
# Para simplificar, representa el saldo mediante un número.
# Permite el acceso solamente si tiene al menos 18 años y el saldo es mayor que 0.
edad2 = int(input("Dime tu edad, otra vez: "))
saldo = int(input("Cual es tu saldo: "))
if edad2 > 18 and saldo > 0:
    print("Acceso permitido")
else:
    print("Acceso denegado")

# Ejercicio 4. Comparar dos números
# Pide al usuario dos números enteros y muestra cuál es mayor.
# Si son iguales, indícalo también.
numero1 = int(input("Escribe un numero: "))
numero2 = int(input("Escribe otro numero: "))
if numero1 > numero2:
    print(numero1, "Es mayor que", numero2)
elif numero1 < numero2:
    print(numero1, "Es menor que", numero2)
else:
    print("Los numeros son iguales")

# Ejercicio 5. Menú con match
# Muestra este menú:
# 1. Crear usuario
# 2. Eliminar usuario
# 3. Salir
# Pide una opción y utiliza match para mostrar la acción seleccionada.
# Para cualquier otro número, muestra:
# Opción incorrecta
print("1. Crear usuario")
print("2. Eliminar usuario")
print("3. Salir")
opcion = int(input("Elige una opción: "))
match opcion:
    case 1:
        print("Crear usuarios")
    case 2:
        print("Eliminar usuario")
    case 3:
        print("Salir")
    case _:
        print("Opcion incorrecta")