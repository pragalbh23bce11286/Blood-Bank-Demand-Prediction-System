import numpy as np
import pandas as pd
import os
import random
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
import tensorflow as tf

dataset = pd.read_csv('/content/Blood Bank Dataset.csv')

X = dataset[['Types of blood','October', 'November', 'December', 'January','February']]
y = dataset[['Output']]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

train_predictions = model.predict(X_train)


input_data=([270,206,173,39,16,17,15,7])

print('Amount of O+ blood required is',int(input_data[0]),"Litres")
print('Amount of A+ blood required is',int(input_data[1]),"Litres")
print('Amount of B+ blood required is',int(input_data[2]),"Litres")
print('Amount of AB+ blood required is',int(input_data[3]),"Litres")
print('Amount of O- blood required is',int(input_data[4]),"Litres")
print('Amount of A- blood required is',int(input_data[5]),"Litres")
print('Amount of B- blood required is',int(input_data[6]),"Litres")
print('Amount of AB- blood required is',int(input_data[7]),"Litres")


data = [270,206,173,39,16,17,15,7]
Blood_Groups = ['O+','A+','B+','AB+','O-','A-','B-','AB-']

plt.figure(figsize=(10, 5))
plt.plot(data,Blood_Groups, marker='o', linestyle='-', color='blue')


plt.title("Required Blood in Next 15 days(in Litres)")
plt.xlabel("Amount of Blood Required(in Litres)")
plt.ylabel("Blood Groups")
plt.grid(True)
plt.show()
