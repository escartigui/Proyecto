#Parte de Daniel

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
                     'precio': precio_nuevo,
                     'stock': stock_nuevo
                 }
                 self.modificador.editar(encontrado, datos_nuevos)
                 print("Producto actualizado correctamente")
             except ValueError:
                 print("El precio y el stock no poseen valores validos. Cancelado operacion")
         else:
             print("Producto no encontrado")
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