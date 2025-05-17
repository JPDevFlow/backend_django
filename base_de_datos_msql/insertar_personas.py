#En este script usaremos la sentencia INSERT para insertar datos en la tabla personas desde python a mysql
# import mysql.connector
import mysql.connector
personas_db = mysql.connector.connect(
    host ="localhost", 
    user ="root",
    password ="admin",
    database ="personas_db"
)

cursor = personas_db.cursor()
sentencia_sql = "INSERT INTO personas(nombre, apellido, edad) VALUES(%s, %s, %s)"#%s es un marcador de posicion
#Los valores que se van a insertar
valores = ("Juan", "Pérez", 30)
    

cursor.execute(sentencia_sql, valores)#execute() ejecuta la sentencia SQL
personas_db.commit()#commit() guarda los cambios en la base de datos

print(f'Se ha agregado el nuevo registro en la db: {valores}')

#Cerramos la conexion
cursor.close()
personas_db.close()