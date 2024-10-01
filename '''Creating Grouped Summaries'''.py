'''Creating Grouped Summaries

 

Write a Python program to add a new column using assign() to the given Data Frame.

Load iris data from the input file.

Print the original Data Frame.

Create a new Data Frame that contain the grouped summary of the input data set based on species_type.

Print the new Data Frame.

 

The input file to be used is iris_with_header.csv file. Note that there is a header row in the input file.

The input file is given as part of the template code.
iris_with_headers.csv
sepal_length,sepal_width,petal_length,petal_width,species_type
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
df=pd.read_csv("iris_with_header.csv")
print("Original DataFrame")
print(df)
grp=df['species_type'].value_counts()
grp_s=grp.reindex(index=["IrisSetosa","IrisVersicolor","IrisVirginica"])
print("species_type")
print(grp_s)