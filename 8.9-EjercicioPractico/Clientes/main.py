from paquete_clientes.modulo_cliente import Cliente
from paquete_clientes.modulo_utilidades import guardar_datos_compras, cargar_datos_compras
from paquete_clientes.modulo_autenticacion import registrar_usuario, login, cargar_datos

datos_clientes = cargar_datos_compras()

cliente1 = Cliente("Cecilia Perdomo", "cecilia.perdomo@gmail.com", 40, ["tecnología", "moda", "farmacia"])

cliente1.comprar("Laptop", "Walmart")
cliente1.comprar("Perfume", "Walmart")
cliente1.comprar("Zapatos", "Amazon")

guardar_datos_compras({cliente1. nombre + " - " + cliente1.email: cliente1.mostrar_historial()})

# Registro y login de usuario
print(registrar_usuario("Cecilia Perdomo", "cecilia.perdomo@gmail.com", 40, ["tecnología", "moda", "farmacia"], "segura123"))
print(login("cecilia.perdomo@gmail.com", "segura123"))

def menu():
    datos_clientes = cargar_datos()
    cliente = None

    while True:
        print("\nMenú de Opciones:")
        print("1. Registrar usuario")
        print("2. Iniciar sesión")
        print("3. Realizar compra")
        print("4. Mostrar historial de compras")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            nombre = input("Nombre: ")
            email = input("Email: ")
            edad = int(input("Edad: "))
            intereses = input("Intereses (separados por coma): ").split(",")
            password = input("Contraseña: ")
            registrar_usuario(nombre, email, edad, intereses, password)
        
        elif opcion == "2":
            email = input("Email: ")
            password = input("Contraseña: ")
            if login(email, password):
                usuario_data = datos_clientes.get(email)
                if usuario_data:
                    cliente = Cliente(
                        nombre=usuario_data.get("nombre", "Desconocido"),
                        email=email,
                        edad=usuario_data.get("edad", 0),
                        intereses=usuario_data.get("intereses", [])
                    )
                    print("Inicio de sesión exitoso.")
                else:
                    print("Usuario no encontrado en la base de datos. Asegúrese de estar registrado correctamente.")
            else:
                print("Credenciales incorrectas.")
        
        elif opcion == "3":
            if cliente:
                producto = input("Ingrese el producto a comprar: ")
                tienda = input("Ingrese la tienda de compra: ")
                cliente.comprar(producto, tienda)
                datos_clientes[cliente.email] = {
                    "nombre": cliente.nombre,
                    "edad": cliente.edad,
                    "intereses": cliente.intereses,
                    "historial": cliente.mostrar_historial()
                }
                guardar_datos_compras(datos_clientes)
                print("Compra realizada con éxito.")
            else:
                print("Debe iniciar sesión primero.")
        
        elif opcion == "4":
            if cliente:
                print("Historial de compras:")
                print(cliente.mostrar_historial())
            else:
                print("Debe iniciar sesión primero.")
        
        elif opcion == "5":
            print("Saliendo del sistema.")
            break
        
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()