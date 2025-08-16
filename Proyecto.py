class Productos:
    def __init__(self, codigo,nombre,categoria,precio,stock):
        self.codigo = codigo
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.stock = stock

    def mostrar_productos(self):
        return f"Codigo{self.codigo},Nombre{self.nombre} Categoria{self.categoria} Precio{self.precio} Stock{self.stock}"

class RegistroProductos:
     def __init__(self):
         self.productos = {}

     def agregar(self):
         try:
             codigo = input("Ingresa el codigo del producto: ")
             if codigo in self.productos:
                 print("el codigo ya existe")
                 nombre = input("Ingresa el nombre del producto: ").strip()
                 if nombre == "":
                     print("el nombre no puede quedar vacio")
                 categoria = input("Ingresa el categoria del producto: ")
                 precio = int(input("Ingresa el precio del producto: "))
                 if precio < 0:
                     print("el precio del producto no puede ser negativo")
                 stock = int(input("Ingresa el stock del producto: "))
                 if stock < 0:
                     print("el stock no puede ser negativo")
         except ValueError:
             print("verifica lo que estas ingresando")