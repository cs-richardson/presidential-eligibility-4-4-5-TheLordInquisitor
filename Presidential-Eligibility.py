#Program written by Son Nguyen
"""
This program prompt the user for their age, their citizenship, and how long
they've been a resident of the U.S to determine if they're eligible to run for
president.
"""

#These 3 lines below prompt the user for inputs
age = int(input("What is your age?: "))
citizenship = input("Are you a citizen of the U.S?: ")
residency = int(input("How long have you been a resident of the U.S?: "))

#These lines determine if the inputs are valid for the user to run for president
if(age >= 35 and citizenship == "yes"  and residency >= 14):
    print ("You are eligible to run for president!")
else:
    print ("You are not eligible to run for president.")
