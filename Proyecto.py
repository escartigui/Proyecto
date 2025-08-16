class Productos:
    def __init__(self, codigo,nombre,categoria,precio,stock):
        self.codigo = codigo
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.stock = stock

    def mostrar_productos(self):
        return f"Codigo {self.codigo},Nombre {self.nombre} Categoria {self.categoria} Precio {self.precio} Stock {self.stock}"

class RegistroProductos:
     def __init__(self):
         self.productos = {}

     def agregar(self):
         try:
                 cantidad = int(input("Ingrese la cantidad de productos que desea guardar: "))
                 for i in range(cantidad):
                     print(f"Producto{i+1}")
                     codigo = input("Ingresa el codigo del producto: ")
                     if codigo in self.productos:
                        print("el codigo ya existe")
                        return self.agregar()
                     if codigo == "":
                         print("El codigo no puede quedar vacio")
                         return self.agregar()
                     nombre = input("Ingresa el nombre del producto: ").strip()
                     if nombre == "":
                        print("el nombre no puede quedar vacio")
                     categoria = input("Ingresa el categoria del producto: ")
                     precio = int(input("Ingresa el precio del producto: "))
                     if precio < 0:
                        print("el precio del producto no puede ser negativo")
                     if precio == "":
                         print("el precio no puede quedar vacio")
                     stock = int(input("Ingresa el stock del producto: "))
                     if stock < 0:
                         print("el stock no puede ser negativo")
                     self.productos[codigo] = Productos(codigo,nombre,categoria,precio,stock)
         except ValueError:
             print("verifica lo que estas ingresando")
     def mostrar(self):
         if not self.productos:
             print("el producto no existe")

         print("\nListado de Productos")
         for categoria, producto in enumerate(self.productos.values(), start=1):
             print(f"{categoria}. {producto.mostrar_productos()}")

registro = RegistroProductos()
while True:
    print("*---Menu---*")
    print("1.Agregar Producto")
    print("2.Mostrar Productos")
    print("3.salir")
    op = int(input("\nIngrese su opción: "))
    match op:
        case 1:
            registro.agregar()
        case 2:
            registro.mostrar()
        case 3:
            print("\nHasta que nos volvamos a ver :3")
            break