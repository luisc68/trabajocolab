##CONECTAR PYTHON A POSTGRES
import psycopg2

try:
    conexion = psycopg2.connect(
        host = 'localhost',
        user = 'postgres',
        password = '1608',
        database = 'cooperativa'
    )
    print('Conexion exitosa')
    cursor=conexion.cursor()
    cursor.execute("SELECT version()")
    row=cursor.fetchone()
    print(row)
    cursor.execute("SELECT numerotransaccion, cuentadeorigen, cuentadedestino, monto, fecha FROM transacciones")
    rows=cursor.fetchall()
    for row in rows:
        print(row)
except Exception as e:
    print('Error de conexion')
    print(e)
finally:
    conexion.close()
    print("Conexion finalizada")
