##Q1.Display Fibonacci Sequence using recursion

##def recur_fibo(n):
##    if n<=1:
##        return n
##    else:
##        return (recur_fibo(n-1) + recur_fibo(n-2))
##
##n=int(input("enter the Number"))
##
##if n <=0:
##    print("please enter a positive number")
##
##else:
##    print("Fibonacci Sequence:")
##    for i in range(n):
##         print(recur_fibo(i))
##output
##enter the Number10
##Fibonacci Sequence:
##0
##1
##1
##2
##3
##5
##8
##13
##21
##34

##Q2.find factoial of number using recursion

##def recur_fctrl(n):
##    if n==1:
##        return n
##    else:
##        return n*recur_fctrl(n-1)
##
##num=int(input("enter a Number :"))
##
##if num<0:
##    print("factorial does not exist for negative number")
##elif num==0:
##    print("factorial of 0 is 1")
##else:
##    print("the factorial of ",num,"is",recur_fctrl(num))
##output
##enter a Number :10
##the factorial of  10 is 3628800

##Q3.calculate body mass index 

##weight=float(input("enter weight in kilogram :"))
##height=float(input("enter height in centimeter:"))
##height=height/100
##bmi=weight/(height*2)
##
##if bmi<18:
##    print("you are underweight"\
##          f"\nbody mass index is {bmi}")
##elif bmi<24:
##    print(f"Body mass index is {bmi}"\
##          f"\nyou are in healthy weight")
##else:
##    print(f"this {bmi} body mass index is"\
##          "overweght")
##output
##enter weight in kilogram :70
##enter height in centimeter:180
##Body mass index is 19.444444444444443
##you are in healthy weight

##Q4.calcuate the natural logarithm of any number

##import math
##
##num=int(input("enter a number"))
##
##print("log value : ",math.log(num))
##output
##enter a number10
##log value :  2.302585092994046

##Q5.program for cube sum of first n natural numbers 

##num=int(input("enter a number : "))
##total=0
##for i in range(1,num+1):
##    total=total+(i*i*i)
##
##print(f"Cube Sum is : {total}")
##output
##enter a number5
##Cube Sum is : 225
