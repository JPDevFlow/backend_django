'''--***PATRON DE DISEÑO DAO***-- DATA- ACCESS- OBJECT
Este patron se utiliza para acceder a la información de una entidad de nuestra aplicacion'''
#deifinimos la clase clientedao que tendra la funcionalidad de interartuar con objetos de tipo cliente
from zona_fit_db.conexion import Conexion
from zona_fit_db.cliente import Cliente
class ClienteDAO:
    SELECCIONAR = "SELECT * FROM clientes ORDER BY id"
    SELECCIONAR_ID = "SELECT *FROM clientes WHERE id=%s"
    INSERTAR = "INSERT INTO clientes(nombre, apellido, membresia) VALUES(%s, %s, %s)"
    ACTUALIZAR = "UPDATE clientes SET nombre=%s, apellido=%s, membresia=%s WHERE id=%s"
    ELIMINAR = "DELETE FROM clientes WHERE id=%s"

    @classmethod
    def seleccionar(cls):

        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            cursor.execute(cls.SELECCIONAR)
            registros = cursor.fetchall()
            #mapeo de clase-table cliente
            clientes = []
            for registro in registros:
                    cliente = Cliente(registro[0],registro[1], registro[2], registro[3])
                    clientes.append(cliente)
            return clientes
        except Exception as e:
            print(f'Ocuirio un error al seleccionar clientes: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def insertar(cls, cliente):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor =conexion.cursor()
            valores = (cliente.nombre, cliente.apellido, cliente.membresia)
            cursor.execute(cls.INSERTAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Ocurrió un error al insertar el cliente: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)


    @classmethod
    def actualizar(cls, cliente):
        conexion = None
        try:
            conexion =Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.nombre, cliente.apellido, cliente.membresia, cliente.id)
            cursor.execute(cls.ACTUALIZAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Ocurrió un error al actualizar el cliente: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)


    @classmethod
    def eliminar(cls, cliente):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores =(cliente.id,)
            cursor.execute(cls.ELIMINAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Ocurrió un error al eliminar el cliente: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def seleccionar_por_id(cls, id):

        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores =(id,)
            cursor.execute(cls.SELECCIONAR_ID, valores)
            registro = cursor.fetchone()
            #mapeo de clase-table cliente
            cliente =  Cliente(registro[0],registro[1], registro[2], registro[3])
            return cliente
        except Exception as e:
            print(f'Ocuirio un error al seleccionar un cliente por id: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

if __name__ == "__main__":
    #Inserta un nuevo cliente
    # cliente1 = Cliente(nombre="alvaro", apellido="puello", membresia= 400)
    # clientes_insertados = ClienteDAO.insertar(cliente1)
    # print(f'Clientes insertados: {clientes_insertados}')

    #Actualizar un cliente
    # cliente_actualizar =Cliente(id=3, nombre="miguel", apellido="puello", membresia= 300)
    # clientes_actualizados = ClienteDAO.actualizar(cliente_actualizar)
    # print(f'Clientes actualizados: {clientes_actualizados}')

    #Eliminar un cliente
    cliente_eliminar =Cliente(id=3)
    clientes_eliminados = ClienteDAO.eliminar(cliente_eliminar)
    print(f'Clientes eliminados: {clientes_eliminados}')
    clientes = ClienteDAO.seleccionar()
    for cliente in clientes:
        print(cliente)