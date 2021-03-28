# 3.1 Write a program to prompt the user for hours and rate per hour using input to compute gross pay. 
# Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours. 
# Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). 
# You should use input to read a string and float() to convert the string to a number. 
# Do not worry about error checking the user input - assume the user types numbers properly.
hours = input("Enter Hours:")
hours = float(hours)
rate = input ("Enter Rate:")
rate = float (rate)
if hours > 40 :
    extra_hours = hours - 40
    gross_pay = 40 * rate
    gross_pay += (extra_hours * (rate*1.5))
    print(gross_pay)
else :
    gross_pay = (hours*rate)
    print(gross_pay)