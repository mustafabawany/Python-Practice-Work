import os
  
input_string = input('Enter elements of a list separated by space(Values of X) ')     #taking value of x
x = input_string.split()

for i in range(len(x)):
     x[i] = float(x[i])                                                             #for conversion into float    

input_string = input('Enter elements of a list separated by space(Values of Y) ')   #taking value of f(x)
y = input_string.split()

for i in range(len(y)):
    y[i] = float(y[i])                                                              #for conversion into float
 
DDT1 = []

for i in range(len(x)):
    k = -1
    for j in range(i+1,len(x)):
        k = k + 1
        # DDT1[i] = (x[j] - x[k]) / (y[j] - y[k])      
        print("i = " , i)
        print("j = " , j)
        print("k = " , k)
        print("\n")
        