import matplotlib.pyplot as plt
import pandas as pd


sales = pd.read_csv("dataset-sell4all.csv") 

result =  sales[1:6]
columnas = sales[0:1]

print(f'Lectura de las 5 primeras lineas \n\r {result} ')
print(f'Las columnas son: {columnas} ')
total_cols = len(sales.Name[1])
print("Numero de columnas: "+str(total_cols))

print('Total de filas:',sales.shape[0])
print (sales.dtypes)
print(sales['Age'].mean()) # media
print(sales['Age'].median()) #mediana
print(sales['Customer spendings'].mean())
print(sales['Customer spendings'].median())

# graficos
plt.bar(sales['Country'],sales['Customer spendings'])
plt.show()
