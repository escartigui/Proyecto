class Productos:
    def __init__(self, codigo,nombre,categoria,precio,stock):
        self.codigo = codigo
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.stock = stock

    def mostrar_productos(self):
        return f"Codigo: {self.codigo},Nombre: {self.nombre} Categoria: {self.categoria} Precio: {self.precio} Stock: {self.stock}"


class RegistroProductos:
     def __init__(self):
         self.productos = {}

     def validacion(self):
             while True:
                 pregunta = input("\ndesea ingresar los datos de nuevo? (si o no): ")
                 if pregunta == "no":
                     break
                 else:
                     return self.agregar()

     def agregar(self):
         try:
                 cantidad = int(input("\nIngrese la cantidad de productos que desea guardar: "))
                 for i in range(cantidad):
                     print(f"Producto {i+1}")
                     codigo = input("Ingresa el codigo del producto: ")
                     if codigo in self.productos:
                        print("el codigo ya existe")
                        return self.validacion()
                     if codigo == "":
                         print("El codigo no puede quedar vacio")
                         return self.validacion()
                     nombre = input("Ingresa el nombre del producto: ").strip()
                     if nombre == "":
                        print("el nombre no puede quedar vacio")
                        return self.validacion()
                     categoria = input("Ingresa el categoria del producto: ")
                     precio = int(input("Ingresa el precio del producto: "))
                     if precio < 0:
                        print("el precio del producto no puede ser negativo")
                        return self.validacion()
                     if precio == "":
                         print("el precio no puede quedar vacio")
                         return self.validacion()
                     stock = int(input("Ingresa el stock del producto: "))
                     if stock < 0:
                         print("el stock no puede ser negativo")
                         return self.validacion()
                     if stock == "":
                         print("el stock no puede quedar vacio")
                         return self.validacion()
                     self.productos[codigo] = Productos(codigo,nombre,categoria,precio,stock)
         except ValueError:
             print("verifica lo que estas ingresando")

     def mostrar(self):
         if not self.productos:
             print("Debes agregar algun producto")

         print("\nListado de Productos")
         for categoria, producto in enumerate(self.productos.values(), start=1):
             print(f"{categoria}. {producto.mostrar_productos()}")

registro = RegistroProductos()
while True:
    print("*---Menu---*")
    print("1.Agregar Producto")
    print("2.Mostrar Productos")
    print("3.salir")
    try:
     op = int(input("\nIngrese su opción: "))
     match op:
        case 1:
            registro.agregar()
        case 2:
            while True:
                print("Menu Listado de Productos")
                print("1.Ordenado por nombre")
                print("2.Ordenado por precio")
                print("3.Ordenado por stock")
                print("4.Mostrar Productos")
                print("5.Regresar")
                try:
                 op = int(input("Ingrese su opción: "))
                 match op:
                     case 1:
                         print("nombres")
                     case 2:
                         print("precios")
                     case 3:
                         print("stocks")
                     case 4:
                        registro.mostrar()
                     case 5:
                         print("Regresando al menu principal")
                         break
                     case _:
                         print("Vuelve a intentarlo")
                except ValueError:
                 print("Debes ingresar correctamente un valor")
        case 3:
            print("\nHasta que nos volvamos a ver :3")
            break
        case _:
            print("Vuelve a intentarlo")
    except ValueError:
        print("Error debes ingresar correctamente una opción")