# Paquete Clientes
Este paquete permite modelar clientes para una página de compras.

## Instalación
```bash
pip install .
```

## Uso
```python
from paquete_clientes import Cliente

cliente = Cliente("Juan", "juan@example.com", 30, ["moda", "tecnología"])
print(cliente)
```

## 📌 **3. Empaquetar y distribuir**
Para crear el paquete, abre la terminal en la carpeta `TuModeloDeClientes/` y ejecuta:

```bash
python setup.py sdist
```
Esto generará un archivo `.tar.gz` dentro de dist/, listo para compartir o instalar con pip install paquete `.tar.gz`.

## 🎯 ¿Por qué usar paquetes redistribuibles?
✅ Permiten instalar y reutilizar tu código fácilmente.
✅ Facilitan compartirlo con otras personas o publicarlo en PyPI.
✅ Mantienen una estructura modular y organizada.