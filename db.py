
from psycopg2 import connect
host="127.0.0.1"
port=5432
dbname="pg_webtareas"
user="postgres"
password="Niag0542"

def cadenaConexion():
    conexion=connect(host=host,port=port,dbname=dbname,
                    user=user,password=password)
    
    return conexion

