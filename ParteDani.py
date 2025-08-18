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
         self.buscador = Busqueda()
         self.modificador = Modificacion()
     def validacion(self):
             while True:
                 pregunta = input("\ndesea ingresar los datos de nuevo? (si o no): ").lower()
                 if pregunta.lower() == "no":
                     break
                 else:
                     return self.agregar()
     def agregar(self):
         try:
                 cantidad = int(input("\nIngrese la cantidad de productos que desea guardar: "))
                 for i in range(cantidad):
                     print(f"Producto {i+1}")
                     codigo = input("Ingresa el codigo del producto: ").lower()
                     if codigo.lower() in self.productos:
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
                     precio = float(input("Ingresa el precio del producto: "))
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
     def ordenar(self):
         if not self.productos:
             print("Debes agregar algun producto")
             return menu()
         print("\nListado de Productos")
         for categoria, producto in enumerate(self.productos.values(), start=1):
          print(f"{categoria}. {producto.mostrar_productos()}")
     def buscar_producto(self):
         objetivo = input("Ingrese el código del producto a buscar: ")
         encontrar = self.buscador.busqueda_secuencial(self.productos, objetivo)
         if encontrar:
             print("\t Producto encontrado")
             print(encontrar.mostrar_productos())
         else:
             print("\t Producto no encontrado")
     def eliminar_producto(self):
         eliminar = input("Ingrese el código del producto a eliminar: ")
         encontrar = self.buscador.busqueda_secuencial(self.productos, eliminar)
         if encontrar:
             print(encontrar.mostrar_productos())
             print("¿Está seguro de eliminar el producto? Si/No")
             respuesta = input("Ingrese si/no: ").upper()
             if respuesta == "SI":
                 self.modificador.eliminar(self.productos, eliminar)
                 print("Producto eliminado correctamente")
             elif respuesta == "NO":
                 print("Operacion cancelada")
             else:
                 print("Opcion no valida. Eliminacion cancelada")
         else:
             print("\t Producto no encontrado")
     def actualizar_producto(self):
         actualizar = input("Ingrese el código del producto que desea editar: ")
         encontrado = self.buscador.busqueda_secuencial(self.productos, actualizar)
         if encontrado:
             print("Producto actual: ")
             print(encontrado.mostrar_productos())
             print("Ingrese los nuevos datos del producto(deje en blanco para no cambiar los datos): ")
             try:
                 precio = input("Ingrese el precio del producto: ")
                 precio_nuevo = float(precio) if precio else encontrado.precio
                 stock = input("Ingrese el stock del producto: ")
                 stock_nuevo = int(stock) if stock else encontrado.stock
                 if precio_nuevo < 0 or stock_nuevo < 0:
                     print("El precio o el stock no puede ser negativo")
                     return
                 datos_nuevos = {
                     'precio ':precio_nuevo,
                     'stock':stock_nuevo,
                 }
                 self.modificador.editar(encontrado, datos_nuevos)
                 print("Producto actualizado correctamente")
             except ValueError:
                 print("\t Error. El precio y el stock deben de ser números positivos")
         else:
             print("Producto no encontrado")
def quick_sort_nombre(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivote = lista[0]
        menores = [x for x in lista[1:] if x.nombre.lower() < pivote.nombre.lower()]
        iguales = [x for x in lista[1:] if x.nombre.lower() == pivote.nombre.lower()]
        mayores = [x for x in lista[1:] if x.nombre.lower() > pivote.nombre.lower()]
        return quick_sort_nombre(menores) + [pivote] + iguales + quick_sort_nombre(mayores)
def quick_sort_precio(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivote = lista[0]
        menores = [x for x in lista[1:] if x.precio < pivote.precio]
        iguales = [x for x in lista[1:] if x.precio == pivote.precio]
        mayores = [x for x in lista[1:] if x.precio > pivote.precio]
        return quick_sort_precio(menores) + [pivote] + iguales + quick_sort_precio(mayores)
def quick_sort_stock(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivote = lista[0]
        menores = [x for x in lista[1:] if x.stock < pivote.stock]
        iguales = [x for x in lista[1:] if x.stock == pivote.stock]
        mayores = [x for x in lista[1:] if x.stock > pivote.stock]
        return quick_sort_stock(menores) + [pivote] + iguales + quick_sort_stock(mayores)
class Busqueda:
    def busqueda_secuencial(self, productos, objetivo):
        for producto in productos.values():
            if producto.codigo.upper() == objetivo.upper():
                return producto
        return None
class Modificacion:
    def eliminar(self, productos, codigo):
        if codigo in productos:
            del productos[codigo]
            return True
        return False
    def editar(self, producto, datos):
        producto.precio = datos['precio']
        producto.stock = datos['stock']
        return True
registro = RegistroProductos()
def menu():
    while True:
      print("\n*---Menu---*")
      print("1.Agregar Producto")
      print("2.Listado de Productos")
      print("3.salir")
      try:
        op = int(input("\nIngrese su opción: "))
        match op:
            case 1:
             registro.agregar()
            case 2:
                while True:
                    print("\nMenu listado de productos")
                    print("1.Mostrar")
                    print("2.Ordenado por nombre")
                    print("3.Ordenado por precio")
                    print("4.Ordenado por stock")
                    print("5.Regresar al menu principal")
                    try:
                     op = int(input("Ingrese su opción: "))
                     match op:
                        case 1:
                         registro.ordenar()
                        case 2:
                            productos_ordenados = quick_sort_nombre(list(registro.productos.values()))
                            print("\nProductos ordenados por nombre:")
                            for i, p in enumerate(productos_ordenados, start=1):
                                print(f"{i}. {p.mostrar_productos()}")
                        case 3:
                             productos_ordenados = quick_sort_precio(list(registro.productos.values()))
                             print("\nProductos ordenados por precio:")
                             for i, p in enumerate(productos_ordenados, start=1):
                                 print(f"{i}. {p.mostrar_productos()}")
                        case 4:
                             productos_ordenados = quick_sort_stock(list(registro.productos.values()))
                             print("\nProductos ordenados por stock:")
                             for i, p in enumerate(productos_ordenados, start=1):
                                 print(f"{i}. {p.mostrar_productos()}")
                        case 5:
                         print("Regresando al menu principal")
                         break
                        case _:
                         print("Vuelve a intentarlo")
                    except ValueError:
                     print("Debes ingresar correctamente un valor")
            case 3:
                registro.buscar_producto()
            case 4:
                while True:
                    print("1. Actualizar producto")
                    print("2. Eliminar producto")
                    eleccion = input("Seleccione una opción: ")
                    if eleccion == "1":
                        registro.actualizar_producto()
                        break
                    elif eleccion == "2":
                        registro.eliminar_producto()
                        break
                    else:
                        print("Debes ingresar correctamente una opcion")
            case 5:
                exit()
            case _:
                print("Vuelve a intentarlo")
      except ValueError:
        print("Error debes ingresar correctamente una opción")
menu()