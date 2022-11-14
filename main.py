##CONECTAR PYTHON A POSTGRES
import psycopg2
import csv
import datetime
import time
import csv2pdf
import schedule
from datetime import datetime
from datetime import date


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
    print("Datos a continuacion")
    print()
    print()
    cursor.execute("SELECT numerotransaccion FROM transacciones")
    rows=cursor.fetchall()
    for row in rows:
        print(row)
    cursor.execute("SELECT cuentadeorigen FROM transacciones")
    rows1=cursor.fetchall()
    for row1 in rows1:
        print(row1)
    cursor.execute("SELECT cuentadedestino FROM transacciones")
    rows2=cursor.fetchall()
    for row2 in rows2:
        print(row2)
    cursor.execute("SELECT monto FROM transacciones")
    rows3=cursor.fetchall()
    for row3 in rows3:
        print(row3)
    cursor.execute("SELECT fecha FROM transacciones")
    rows4=cursor.fetchall()
    for row4 in rows4:
        print(row4)
        print()
        print()
except Exception as e:
    print('Error de conexion')
    print(e)
finally:
    conexion.close()
    print("Conexion finalizada")



with open('test.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    ##now = datetime.datetime.now()
    #print(now.strftime("%Y-%m-%d %H:%M:%S"))
    writer.writerow(['numero de transaccion', '  originaria  ', '  recipiente  ', '  monto  ', 'fecha'])
    writer.writerow([row, row1, row2,row3, row4])
    writer.writerow([ row, row1, row2,row3, row4])
    writer.writerow([ row, row1, row2,row3, row4])

with open('test.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row6 in reader:
        print(row6)

#now2 = datetime.now()

from csv2pdf import convert
convert("test.csv", "2022-11-15.pdf")



