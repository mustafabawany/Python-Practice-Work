# 9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of 
# mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person 
# who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count 
# of the number of times they appear in the file. After the dictionary is produced, the program reads through 
# the dictionary using a maximum loop to find the most prolific committer.

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

            #It automatically checks for most common word

            counts[words[1]] = counts.get(words[1],0) + 1                           
    
    #Checking for most common word used

    bigcount = None
    bigword = None
    for key,value in counts.items():
        if bigcount is None or value > bigcount:
            bigword = key
            bigcount = value
    print(bigword,bigcount)

except:
    print("File Doesnot Exits.")
    quit()