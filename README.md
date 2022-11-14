# trabajocolab
Ejercicio 2
Instrucciones
Use las tecnicas, patrones, librerias e idas (o extensiones de todos estos) aprendidas de los
capítulos del libro: Automate the Boring Stuff with Python.
- Nuevo Capitulo: Capitulo 17 - Manejo de tiempo, programando tareas y abrir
programas
- Libreria: PyPlot
- Git
- GitHub
Usar un solo repositorio alojado en GitHub donde la versión final del codigo se encuentre en el
branch principal (Main o Master).
Descripción del problema
La misma cooperativa del sector educación aun no planea incluir un modulo de contabilidad a
su sistema por un tema de costos, pero, requieren de los datos del sistema para que sus
contadores puedan hacerlo.
Para que esto sea posible se ocupa que todos los días a las 8AM, se generan los siguientes
reportes del sistema, de forma automática y en el siguiente orden:
1. Se obtienen todas las transacciones de la base de datos con fecha del dia anterior.
2. Se hace un documento .CSV con las siguientes columnas:
Numero de
Transaccion
Originaria Recipiente Monto Fecha
- La cuenta originaria y recipiente son representadas por su número de cuenta (no
ID).
- La fecha tiene fecha y hora.
3. Se exporta el documento .CSV a PDF ambos con nombre del dia que se genero en
formato DD-MM-YYYY y este se guarda dentro de la carpeta /Documentos (windows).
4. Usando PyPlot genere los gráficos: Tamaño de Transacciones y Cuentas más activas.
Coloque ambos en un solo documento .PDF y guárdelo dentro de la carpeta
/Documentos/Gráficos (en windows) con nombre del dia en que se genero con formato
DD-MM-YYYY.
a. Tamaño de transacciones: Para propósitos de gerencia y finanzas, se necesita
visualizar dia a dia el volumen de transacciones por las categorías de tamaño,
un transacción entra dentro de una categoría dependiendo del monto de esta.
Usar grafico de pie o similar.
Categorias:
i. Transacciones de $0.01 a $10.
ii. Transacciones de $10.01 a $50.
iii. Transacciones de $50.01 a $200.
iv. Transacciones de $200.01 a $500.
v. Transacciones de $500.01 a $1500.
vi. Transacciones en exceso de $1500.01.
Ejemplo: Si una transaccion tiene un monto de $300, entra en la
categoria 4, entre $200.01 a $500.
b. Cuentas más activas: Por tema de seguridad y prevencion de fraude se requiere
de un grafico donde se vean todas las cuentas que hacen transacciones arriba
de los $1500.01 y la cantidad de transacciones que hicieron. Use un grafico de
barras.
5. Guarde en un archivo .CSV con formato DD-MM-YYYY de la fecha en que se genero,
en 2 tablas los datos de los 2 graficos descritos en el paso anterior en la misma carpeta
que el documento PDF.
