import csv
import datetime
import time
import csv2pdf
import schedule
from datetime import datetime
from datetime import date


#(ejemplos y pruebas, ademas de creacion del archivo csv)
with open('test.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    now = datetime.datetime.now()
    print(now.strftime("%Y-%m-%d %H:%M:%S"))
    writer.writerow(['numero de transaccion', '  originaria  ', '  recipiente  ', '  monto  ', 'fecha'])
    writer.writerow(['          1          ', '  Paul      ', '  5000-uc-12  ', '  100  ', now])
    writer.writerow(['          2          ', '  Bob       ', '  52040-ll-32  ', '  545 ', now])
    writer.writerow(['          3          ', '  Jordan    ', '  2345-uuu-2  ', '  1123 ', now])

with open('test.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)
#convertir csv a pdf
from csv2pdf import convert
convert("test.csv", "2022-11-15.pdf")
