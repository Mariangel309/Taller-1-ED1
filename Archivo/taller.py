ventas = []

def mostrar_menu():
    print(" -MENÚ- ")
    print("1. Crea una nueva venta")
    print("2. Listar venta")
    print("3. Buscar por ID")
    print("4. Modificar")
    print("5. Eliminar")
    print("6. Calcular ingreso total")
    print("7. Salir")

while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        print("Crear venta")
        try:
            id_venta = int(input("ID de la venta: "))
            existe = False
            for venta in ventas:
                if venta[0] == id_venta:
                    existe = True
                    break
            if existe:
                print("Ya se encuentra una venta con ese ID")
            
            else:
                producto = input("Digite el nombre del producto: ")
                cantidad = int(input("Digite la cantidad: "))
                precio_unitario = float(input("Precio unitario: "))
                nueva_venta = [id_venta, producto, cantidad, precio_unitario]
                ventas.append(nueva_venta)
                print("Venta registrada!")
        #Validación
        except ValueError:
            print("Input inválido")
            
    elif opcion == "2":
        if len(ventas) == 0:
            print("No hay ventas registradas")
        else:
            for venta in ventas:
                id_venta = venta[0]
                producto = venta[1]
                cantidad = venta[2]
                precio_unitario = venta[3]
                total = cantidad + precio_unitario
                print(f"ID: {id_venta} | producto: {producto} | cantidad: {cantidad} | precio unitario: {precio_unitario} | total: {total}")

    elif opcion == "3":
        print("Buscar venta por ID")
        try:
            id_buscar = int(input("Ingresa el ID de la venta a buscar: "))
            encontrada = False
            for venta in ventas:
                if venta[0] == id_buscar:
                    print(f"ID: {venta[0]} | Producto: {venta[1]} | Cantidad: {venta[2]} | Precio unitario: {venta[3]} | Total: {venta[2]+venta[3]}")
                    encontrada = True
                    break
            if not encontrada: 
                print("No se encontró ninguna venta con el ID digitado")
        except ValueError:
            print("ID ingresado no válido")
    elif opcion == "4":
        print("Modificar")
        try:
            id_modificar = int(input("Ingresa el ID de la venta que desea modificar: "))
            modificada = False
            for i in range(len(ventas)):
                if ventas[i][0] == id_modificar:
                    print("Venta actual: {ventas[i]}")
                    nuevo_producto = input("Nuevo nombre del producto: ")
                    nueva_cantidad = int(input("Nueva cantidad: "))
                    nuevo_precio = float(input("Nuevo precio unitario: "))

                    ventas[i][1] = nuevo_producto
                    ventas[i][2] = nueva_cantidad
                    ventas[i][3] = nuevo_precio

                print("Venta modificada con éxito.")
                modificada = True
                break
            if not modificada:
                print("No se encontró ninguna venta con ese ID.")
        except ValueError:
            print("ingrese datos válidos.")



    elif opcion == "5":
        print("Eliminar")
        try:
            id_eliminar = int(input("Ingrese el ID de la venta que desea eliminar: "))
            eliminada = False
            for i in range(len(ventas)):
                if ventas[i][0] == id_eliminar:
                    print(f"Venta encontrada: {ventas[i]}")
                    confirmar = input("¿Seguro que desea eliminarla? (s/n): ")
                    if confirmar.lower() == "s":
                        ventas.pop(i)
                        print("venta eliminada con éxito.")
                    else:
                        print("eliminación cancelada.")
                    eliminada = True
                    break
            if not eliminada:
                print("No se encontró ninguna venta con ese ID.")
        except ValueError:
            print("ingrese un ID válido.")
        
    elif opcion == "6":
        print("Calcular ingreso total")
        if len(ventas) == 0:
            print("No hay ventas registradas.")
        else:
            total_ingresos = 0
            for venta in ventas:
                total_ingresos += venta[2] * venta[3]
            print(f"El ingreso total es: {total_ingresos}")

    elif opcion == "7":
        print("Salir")
        break
    else:
        print("Opcion no válida")



