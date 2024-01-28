##Q1.Program to find the factorial of a Number
##
##num=int(input("Enter the Number"))
##
##fctrl=1
##
##if num<0:
##    print("Factorial does not exist for negative number")
##elif num==0:
##    print("Factorial of 0 is 1")
##else:
##    for i in range(1,num+1):
##        fctrl=fctrl*i
##    print(f"the factorial of {num} is {fctrl}")
##output
##Enter the Number4
##the factorial of 4 is 24
##Enter the Number5
##the factorial of 5 is 120

##Q2.program to display multiplication table

##num=int(input("Enter the Number"))
##total=0
##print(f"Table of {num}")
##for i in range(1,11):
##    total=total+num
##    print(total)
##output
##Enter the Number5
##Table of 5
##5
##10
##15
##20
##25
##30
##35
##40
##45
##50
##program end
##print("program end")

##Q3. program to print fibonacci sequece

##num=int(input("Enter the Number"))
##total=0
##num1=0
##num2=1
##print("Fibonacci Number")
##for i in range(1,num+1):
##    total=num1+num2
##    num1=num2
##    num2=total
##    print(total)
##output
##Enter the Number10
##Fibonacci Number
##1
##2
##3
##5
##8
##13
##21
##34
##55
##89

##Q4.program to check armstrong Number

##num=int(input("enter a number: "))
##
##sum1=0
##
##temp=num
##while temp>0:
##    digit=temp%10
##    sum1=sum1+digit**3
##    temp //=10
##
###display result
##if num==sum1:
##    print(num,"is an armstrong number")
##else:
##    print(num,"is not an armstrong number")
##output
##enter a number: 6363
##6363 is not an armstrong number
##enter a number: 153
##153 is an armstrong number

##Q5.program to find the sum of Natural Numbers

##num=int(input("enter the number"))
##
##total=0
##for i in range(1,num+1):
##    total=total+i
##print(f"Sum of {num} is {total}")
##
##output
##enter the number10
##Sum of 10 is 55

