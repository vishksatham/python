'''
Name: fibonacci.py
Author: Raj Gopinath
Date: 06/06/2023 
Purpose: fibonacci series
0,1,1,2,3,5,8...n
'''
i=0
nextValue=1
while i<=1000:
     print(i)
     prevValue=i
     i = i + nextValue
     nextValue = prevValue
'''
Exercise: negative fibonacci 
'''

i=0
nextValue=1
while i<=1000:
     print(-i)
     prevValue=i
     i = i + nextValue
     nextValue = prevValue


