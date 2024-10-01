'''Bank Transactions

A bank account has had withdrawals and deposits tracked in a numpy array called account_transactions. Based on this list of account transactions, what is the total remaining in the account? Deposits are represented by positive numbers and withdrawals are represented by negative numbers.Can you write a Python program to solve the above problem? Transaction values is considered to be of type float.

Refer Sample Input and Output for formatting specifications.
All text in bold corresponds to input and the rest corresponds to output.

Sample Input and Output :
Enter the number of transactions
5
Enter the value of each transaction
10000
-5000
2000
-3000
-500
Remaining Amount
3500.0'''
import numpy as np 
size=int(input("Enter the number of transactions"))
lst=[ ]
print("\nEnter the value of each transaction")
for i in range (size):
    ele=float(input())
    lst.append(ele)

arr=np.array(lst)
total=np.sum(lst)
print("Remaining Amount")
print(total)