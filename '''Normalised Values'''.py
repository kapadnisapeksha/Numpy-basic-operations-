'''Normalised Values

Write a Python program to find the normalised values of the sepal length column (first column of the iris dataset)
Read data from a csv file. The input file is provided as part of the template code. File name is iris.csv.
Refer Sample Output for formatting Specifications. All float values in the output array are rounded to 3 decimal places using round() function.

Sample Output :
Sepal Length
[5.1 4.9 4.7 5.  7.  6.4 6.9 6.3 5.8 7.1]
Normalized Sepal Length
[0.167 0.083 0.    0.125 0.958 0.708 0.917 0.667 0.458 1.   ]
iris.csv
5.1,3.5,1.4,0.2,IrisSetosa
4.9,3.0,1.4,0.2,IrisSetosa
4.7,3.2,1.3,0.2,IrisSetosa
5.0,3.3,1.4,0.2,IrisSetosa
7.0,3.2,4.7,1.4,IrisVersicolor
6.4,3.2,4.5,1.5,IrisVersicolor
6.9,3.1,4.9,1.5,IrisVersicolor
6.3,3.3,6.0,2.5,IrisVirginica
5.8,2.7,5.1,1.9,IrisVirginica
7.1,3.0,5.9,2.1,IrisVirginica


'''
import pandas as pd
import numpy as np
df = pd.read_csv('iris.csv', names=['Sepal_length', 'Sepal_width', 'Petal_length', 'Petal_width', 'Species'])


sepal_length=df['Sepal_length'].values[0:10]
print("Sepal Length")
print(sepal_length)
normalised=(sepal_length-sepal_length.min())/(sepal_length.max()-sepal_length.min())
print("Normalized Sepal Length")
print(np.round(normalised[:10],3))