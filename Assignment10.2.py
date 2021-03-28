# 10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day 
# for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then 
# splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
filename = input("Enter file name: ")

try:
    fhand = open(filename,'r')
    counts = dict()
    for line in fhand:      

        #Used for checking the starting word

        if not line.startswith("From ") :                                           
            continue
        else :
            words = line.split()

            #It automatically checks for most common time (hour)

            time = words[5].split(":")
            counts[time[0]] = counts.get(time[0],0) + 1    

    #Sorting dictionary using tuples

    t = sorted(counts.items())
    
    for k,v in sorted(counts.items()):
        print(k,v)
    

except:
    print("File Doesnot Exits.")
    quit()