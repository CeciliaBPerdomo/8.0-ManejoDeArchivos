# paquete_clientes/modulo_autentication.py
import json

def guardar_datos(datos, archivo="clientes.json"):
    try: 
        with open(archivo, "w") as file:
            json.dump(datos, file, indent=4)
    except FileNotFoundError:
        return (f"El archivo {archivo} no existe.")
    except json.decoder.JSONDecodeError:
        return (f"El archivo {archivo} está vacío.")
    except Exception as e:
        return (f"Error: {e}")
    else: 
        return "Datos guardados correctamente."

def cargar_datos(archivo="clientes.json"):
    try:
        with open(archivo, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print (f"El archivo {archivo} no existe. Se devolverá un diccionario vacío.")
        return {}
    except json.decoder.JSONDecodeError:
        print (f"El archivo {archivo} está vacío. Se devolverá un diccionario vacío.")
        return {}
    except Exception as e:
        print (f"Error: {e}")
        return {}
    else:
        print ("Datos cargados correctamente.")

def registrar_usuario(nombre, email, edad, intereses, contraseña, archivo="clientes.json"):
    try:
        usuarios = cargar_datos(archivo)
        if email in usuarios:
            return "El usuario ya está registrado."
        usuarios[email] = {
            "nombre": nombre, 
            "edad": edad, 
            "intereses": intereses, 
            "contraseña": contraseña
        }
        guardar_datos(usuarios, archivo)
    except FileNotFoundError:
        return f"El archivo {archivo} no existe."
    except Exception as e:
        return f"Error: {e}"
    else:
        return "Registro exitoso."

def login(email, contraseña, archivo="clientes.json"):
    try:
        usuarios = cargar_datos(archivo)
        if email in usuarios and usuarios[email]["contraseña"] == contraseña:
            return "Inicio de sesión exitoso."
        return "Credenciales incorrectas."
    except FileNotFoundError:
        return f"El archivo {archivo} no existe."
    except Exception as e:
        return f"Error: {e}"