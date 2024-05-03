'''CHECK LEAP YEAR OR NOT USING IF..ELIF..ELSE STATEMENT'''

year = int(input("Enter year: "))
if(year % 400 == 0):
    print(year, "It's a leap year!!")
elif(year % 4 == 0 and year % 100 ==0):
    print(year, "It's a leap year!!")
else:
    print(year, "Not a leap year!!")
