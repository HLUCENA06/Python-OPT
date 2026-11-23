coche = {
    "marca": "Seat",
    "modelo": "Ateca",
    "color": "blanco",
    "kilometros": 125000
}

# muestra el diccionario completo
print("coche:", coche)

#Acceder a un valor mediante su clave
print(coche["color"])
#Tambien sirve
print(coche.get("modelo"))
#La diferencia es que si la clave no existe, [] devuelve KeyError mientras que .get devuelve None

#Recorrer el diccionario
print("Bucle for que recorre diccionario")
for clave in coche:
    print(" *", clave, "=>", coche[clave])

#Modificar un valor
coche["color"] = "gris" #Como el valor de color es blanco, pasa a ser gris
#Tambien se puede usar
coche.update({"kilometros": 99999})

#Añadir un valor
coche["taller"] = "Alterio reparaciones"

#Diccionario con una lista como valor
servidor = {
    "nombre": "web01",
    "ip": "192.168.1.20",
    "servicios": ["ssh", "http", "https"]
}

#Lista cuyos elementos son diccionarios
servidores = [
    {
        "nombre": "web01",
        "ip": "192.168.1.20"
    },
    {
        "nombre": "db01",
        "ip": "192.168.1.30"
    },
    {
        "nombre": "backup01",
        "ip": "192.168.1.40"
    }
]