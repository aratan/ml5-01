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

#filtro elimina las ventas menos de 10€
#mixto sales = sales.loc[~((sales['Customer spendings'] == 0) | (sales['Age'] == 0))]
sales = sales[sales['Customer spendings'] < 10]
print(sales)

#elimina las filas duplicadas 
sales = sales.drop_duplicates()
print(sales)


#Elimina vacias
sales = sales.dropna()

print(sales)

# graficos
plt.bar(sales['Country'],sales['Customer spendings'])
plt.show()

#deja solo Country, Age, Gender, Customer spendings
##sales.drop(axis=1, columns='Name')
sales =  sales.drop(axis=1, columns=['Name','Phone number','Email','Address','Postal code','Last date of connection','Last time of connection'])
####['Name','Country','Age','Score','Scholarship'])
print(sales)

# Create DataFrame
data = pd.DataFrame(sales)

# Write to CSV file
data.to_csv("Customers.csv")

# Print the output.
print(data)
