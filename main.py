import matplotlib.pyplot as plt
  
# year contains the x-axis values
# and e-india & e-bangladesh
# are the y-axis values for plotting  
  
year = ["I", 'II', "III", "IV", "V","VI"]
e_india = [100.6, 158.61, 305.54, 394.96, 724.79, 800]
e_bangladesh = [10.5, 25.21, 58.65, 119.27, 274.87, 800]
  
# plotting of x-axis(year) and 
# y-axis(power consumption)
#with different colored labels of two countries 
  
plt.plot(year, e_india, color ='orange', 
         label ='Empresa1')
  
plt.plot(year, e_bangladesh, color ='g', 
         label ='Empresa2')
  
# naming of x-axis and y-axis
plt.xlabel('Categorias')
plt.ylabel('Transacciones')
  
# naming the title of the plot
plt.title('Cantidad de Transacciones por categoria')
  
plt.legend()
plt.show()