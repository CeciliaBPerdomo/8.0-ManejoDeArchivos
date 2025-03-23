# paquete_clientes/modulo_utilidades.py
import json

def guardar_datos_compras(datos, archivo="clientes_compras.json"):
    try:
        with open(archivo, "w") as file:
            json.dump(datos, file, indent=4)
    except FileNotFoundError:
        return "El archivo no existe."
    except Exception as e:
        return f"Error: {e}"
    else:
        return "Datos guardados correctamente."

def cargar_datos_compras(archivo="clientes_compras.json"):
    try:
        with open(archivo, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return "El archivo no existe."
    except Exception as e:
        return f"Error: {e}"
    else:
        return "Datos cargados correctamente."