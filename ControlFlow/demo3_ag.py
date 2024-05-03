'''REVERSE THE DIGITS OF A GIVEN NUMBER USING WHILE LOOP'''

n1 = int(input("Enter number: "))
rev = 0
while(n1>0):
    remainder = n1 % 10
    rev = remainder + (rev * 10)
    n1 = n1 // 10
print("The Reversed number is: ",rev)
