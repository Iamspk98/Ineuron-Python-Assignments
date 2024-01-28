##Q1.check no is posotive , negative or Zero
##num1=int(input("enter the Number:"))
##
##if num1<0:
##    print(f"{num1} is negative")
##elif num1==0:
##    print(f"{num1} is Zero")
##else:
##    print(f"{num1} is Poositive")
##output
##enter the Number:3
##3 is Poositive

##Q2.check no is even or odd
##num1=int(input("enter the Number:"))
##
##if num1%2==0:
##    print(f"{num1} is Even")
##else:
##    print(f"{num1} is Odd")
##output
##enter the Number:4
##4 is Even

##Q3.check prime number
##num1=int(input("enter the Number:"))
##count=0
##li=[2,3,5]
##for i in li:
##    if num1%i==0:
##        count=1
##
##if count == 1:
##    print(f"{num1} is not prime")
##else:
##    print(f"{num1} is prime")
##output
##enter the Number:4
##4 is not prime
##enter the Number:47
##47 is prime

##Q4.check leap year
##year=int(input("enter the Year:"))
##
##if year%4==0:
##    print(f"{year} is Leap year")
##else:
##    print(f"{year} is not Leap year")
##
##output
##enter the Year:2023
##2023 is not Leap year
##enter the Year:2024
##2024 is Leap year

##Q5.prime no in interval of 1-10000 
##
##count=0
##li=[2,3,5]
##for i in range(2,101):
##    for j in range(2,101):
##        if i%j==0:
##            break
##    if i==j:
##        print(i,end=" ")
##output
##2 3 5 7 11 13 17 19 23 29 31
##37 41 43 47 53 59 61 67 71 73 79 83 89 97 








