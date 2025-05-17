#Esta seria la capa de presentacion, lo que veria el usario en pan
from zona_fit_db.cliente_dao import ClienteDAO
from zona_fit_db.cliente import Cliente
print("***CLIENTES ZONA FIT (GYM)***")

opcion = None
while opcion != 5:
    print('''***\\MENU PRINCIPAL\\***
          1. Listar clientes
          2. Agregar cliente
          3. Actualizar cliente
          4. Eliminar cliente
          5. Salir''')
    opcion = int(input("Seleccione una opción (1-5): "))
    if opcion == 1: #listar clientes
        clientes =ClienteDAO.seleccionar()
        print("--LISTADO DE CLIENTES--")
        for cliente in clientes:
            print(cliente)
    elif opcion == 2: #agregar cliente
        nombre_var =input("Ingrese el nombre del cliente: ")
        apellido_var =input("Ingrese el apellido del cliente: ")
        membresia_var =input("Ingrese la membresia del cliente: ")
        cliente =Cliente(nombre=nombre_var, apellido=apellido_var, membresia=membresia_var)
        clientes_insertados =ClienteDAO.insertar(cliente)
        print(f"Se insertaron {clientes_insertados} clientes")
    elif opcion == 3: #actualizar cliente
        id_cliente_var =int(input("Ingrese el id del cliente a actualizar: "))
        nombre_var =input("Ingrese el nuevo nombre del cliente: ")
        apellido_var =input("Ingrese el nuevo apellido del cliente: ")
        membresia_var =input("Ingrese la nueva membresia del cliente: ")
        cliente =Cliente(id_cliente_var, nombre_var, apellido_var, membresia_var)
        clientes_actualizados =ClienteDAO.actualizar(cliente)
        print(f"Se actualizaron {clientes_actualizados} clientes")
    elif opcion == 4: #eliminar cliente
        id_cliente_var = int(input("Ingrese el id del cliente a eliminar: "))
        cliente =Cliente(id_cliente_var)
        clientes_eliminados =ClienteDAO.eliminar(cliente)
        print(f"Se eliminaron {clientes_eliminados} clientes")
    else:
        print("has salido del programa, hasta pronto...")