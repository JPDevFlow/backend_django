#usaremos la sentencia DELETE para eliminar datos en la tabla personas desde python a mysql
#En este caso la base de datos se llama personas_db
import mysql.connector
personas_db = mysql.connector.connect(
    host ="localhost", 
    user ="root",
    password ="admin",
    database ="personas_db"
)

cursor = personas_db.cursor()
sentencia_sql = "DELETE FROM personas WHERE ID =%s"
valores =(6,)
cursor.execute(sentencia_sql, valores)
personas_db.commit()#commit() guarda los cambios en la base de datos
print(f'Se ha eliminado el registro en la db: {valores}')
#Cerramos la conexion
cursor.close()
personas_db.close()