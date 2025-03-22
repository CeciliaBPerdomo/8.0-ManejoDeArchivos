# paquete_clientes/modulo_autentication.py
import json

def guardar_datos(datos, archivo="clientes.json"):
    with open(archivo, "w") as file:
        json.dump(datos, file, indent=4)

def cargar_datos(archivo="clientes.json"):
    try:
        with open(archivo, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def registrar_usuario(nombre, email, edad, intereses, contraseña, archivo="clientes.json"):
    usuarios = cargar_datos(archivo)
    if email in usuarios:
        return "El usuario ya está registrado."
    usuarios[email] = {"nombre": nombre, "edad": edad, "intereses": intereses, "contraseña": contraseña}
    guardar_datos(usuarios, archivo)
    return "Registro exitoso."

def login(email, contraseña, archivo="clientes.json"):
    usuarios = cargar_datos(archivo)
    if email in usuarios and usuarios[email]["contraseña"] == contraseña:
        return "Inicio de sesión exitoso."
    return "Credenciales incorrectas."