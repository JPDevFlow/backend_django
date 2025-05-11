import mysql.connector
#Creamos un objeto de conexion a la base de datos
#En este caso la base de datos se llama personas_db
personas_db = mysql.connector.connect(
    host ="localhost", #127.0.0.1
    user ="root",
    password ="admin",
    database ="personas_db"
)
#Ejecurtar la sentencia SELECT
#para ello creamos un objeto cursor
cursor = personas_db.cursor()
cursor.execute("SELECT * FROM personas");
#Obtenemos todos los registros
resultados = cursor.fetchall()#El metodo fetchall() devuelve todos los registros de la consulta
#Iteramos sobre los resultados
for persona in resultados:
    print(persona)

#Cerramos la conexion
cursor.close()
personas_db.close()
