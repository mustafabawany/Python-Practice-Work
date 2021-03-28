import array as arr

a = arr.array('i', [1,2,3]) 

print ("The new created array is : ") 
for i in range (0, 3): 
	print (a[i]) 

b = arr.array('d', [2.5, 3.2, 3.3]) 

print ("The new created array is : ")   
for i in range (0, 3): 
	print (b[i]) 