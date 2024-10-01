'''
Unique Values
Write a Python program to find the unique values and the count of unique values in the species column (last column of the iris dataset)
Read data from a csv file. The input file is provided as part of the template code.File name is iris.csv.
Refer Sample Output for formatting Specifications.
Sample Output :

Unique Values in Iris Species
IrisSetosa
IrisVersicolor
IrisVirginica
Unique Values Count
3'''
import pandas as pd 
data = pd.read_csv('iris.csv')

species=data.iloc[:,-1]

uniq_cnt=species.unique()
print("Unique Values in Iris Species")
for i in uniq_cnt:
    print(i)
# print(uniq_cnt,sep='\n')

cnt=len(uniq_cnt)
print("Unique Values Count")
print(cnt)