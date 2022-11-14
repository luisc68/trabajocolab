from matplotlib import pyplot as plt
import json

transacciones = json.load(open('data.json', 'r'))
xAxis = [key for key, value in transacciones.items()]
yAxis = [value for key, value in transacciones.items()]
plt.grid(True)

plt.plot(xAxis,yAxis, color='maroon', marker='o')
plt.xlabel('variable')
plt.ylabel('value')

fig = plt.figure()
plt.bar(xAxis,yAxis, color='maroon')
plt.xlabel('variable')
plt.ylabel('value')

plt.show()
