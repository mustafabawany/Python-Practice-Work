fhand = open ('temp.txt')
for iteration in fhand:
    # print(iteration)
    if iteration.startswith("My"):
        print(iteration)
