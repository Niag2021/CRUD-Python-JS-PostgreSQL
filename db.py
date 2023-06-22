
from psycopg2 import connect
host="0.0.0.0"
port=5432
dbname="pg_webtareas"
user="postgres"
password="Niag0542"

def cadenaConexion():
    conexion=connect(host=host,port=port,dbname=dbname,
                    user=user,password=password)
    
    return conexion

