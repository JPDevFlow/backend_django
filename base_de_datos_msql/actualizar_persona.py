#Usaremos la sentencia UPDATE para actualizar datos en la tabla personas desde python a mysql
#En este caso la base de datos se llama personas_db
#Creamos el objeto de tipo conexion para conectarnos a la base de datos de mysql
import mysql.connector
personas_db = mysql.connector.connect(
    host ="localhost", 
    user ="root",
    password ="admin",
    database ="personas_db"
)

cursor = personas_db.cursor()
#Creamos la sentencia SQL para actualizar los datos
sentencia_sql = "UPDATE personas SET nombre = %s, apellido = %s, edad = %s WHERE id = %s"
valores = ("daviña", "gomez", 27, 7)

cursor.execute(sentencia_sql, valores)
personas_db.commit()#commit() guarda los cambios en la base de datos
print(f'Se ha actualizado el registro en la db: {valores}')
#Cerramos la conexion
cursor.close()
personas_db.close()