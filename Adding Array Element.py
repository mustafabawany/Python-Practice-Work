import array as arr
numbers = arr.array('i',[1,2,3])
numbers.append(5)
for i in range(0,4):
    print(numbers[i])