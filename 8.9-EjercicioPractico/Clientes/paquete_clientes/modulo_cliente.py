# paquete_clientes/modulo_cliente.py
class Cliente:
    def __init__(self, nombre, email, edad, intereses):
        self.nombre = nombre
        self.email = email
        self.edad = edad
        self.intereses = intereses
        self.historial_compras = []

    def __str__(self):
        return f"Cliente: {self.nombre}, Email: {self.email}, Edad: {self.edad}"

    def comprar(self, producto, tienda):
        self.historial_compras.append((producto, tienda))
        return f"{self.nombre} ha comprado {producto} en {tienda}."

    def mostrar_historial(self):
        return self.historial_compras