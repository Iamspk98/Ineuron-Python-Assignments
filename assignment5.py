##Q1.program to find LCM

##num1=int(input("enter the first number:"))
##num2=int(input("enter the second number:"))
##
##def lcm1 (num1,num2):
##    if num1>num2:
##        greater=num1
##    else:
##        greater=num2
##
##    while True:
##        if ((greater%num1==0) and (greater%num2==0)):
##            lcm=greater
##            break
##        greater +=1
##    return lcm
##output=lcm1(num1,num2)
##print(f"the LCM is : {output}") 
##output
##enter the first number:20
##enter the second number:30
##the LCM is : 60

##Q2.program to find HCF

##num1=int(input("enter the first number:"))
##num2=int(input("enter the second number:"))
##
##def hcf(num1,num2):
##    if num1<num2:
##        fctrl=num1
##    else:
##        fctrl=num2
##    while True:
##        if((num1%fctrl==0)and(num2%fctrl==0)):
##            hcf1=fctrl
##            break
##        fctrl -=1
##    return hcf1
##output=hcf(num1,num2)
##print(f"HCF of given numbers is {output}")
##output
##enter the first number:100
##enter the second number:200
##HCF of given numbers is 100

##Q3.program to convert decimal to binary , octa,hexadecimal

##num=int(input("enter the number"))
##print("Decimal number is",num)
##print(bin(num),"in binary")
##print(oct(num),"in octal")
##print(hex(num),"in hexadecimal")
##output
##enter the number16
##Decimal number is 16
##0b10000 in binary
##0o20 in octal
##0x10 in hexadecimal

#Q4.program to find the ASCII value of character

##chr1=str(input("enter the character in CAPITAL letter"))
##chr2=str(input("enter the character in small letter"))
##print(f"the ASCII value of {chr1} is ",ord(chr1))
##print(f"the ASCII value of {chr2} is ",ord(chr2))
##output
##enter the character in CAPITAL letterA
##enter the character in small lettera
##the ASCII value of A is  65
##the ASCII value of a is  97

##Q5.program of calculator with 4 basic operations
##
##def addition(num1,num2):
##    total=num1+num2
##    return total
##
##def subtraction(num1,num2):
##    total=num1-num2
##    return total
##
##def division(num1,num2):
##    total=num1//num2
##    return total
##
##def multiplication(num1,num2):
##    total=num1*num2
##    return total
##
##
##while True:
##    input1=int(input(f"\nenter the opertion number "\
##                    f"want to perform"\
##                    f"\n1.Addition"\
##                    f"\n2.Subtraction"\
##                    f"\n3.Division"\
##                    f"\n4.Multiplication"\
##                    f"\nEnter your choice: "))
##    #taking input from user
##    num1=int(input("Enter first number"))
##    num2=int(input("Enter second number"))
##    #calling functions using conditional statement
##    if input1==1:
##        output=addition(num1,num2)
##        print(f"Addition of {num1},{num2} is {output}")
##    elif input1==2:
##        output=subtraction(num1,num2)
##        print(f"Subtraction of {num1},{num2} is {output}")
##    elif input1==3:
##        output=division(num1,num2)
##        print(f"Division of {num1},{num2} is {output}")
##    elif input1==4:
##        output=multiplication(num1,num2)
##        print(f"Multiplication of {num1},{num2} is {output}")
##        
##output
##enter the opertion number want to perform
##1.Addition
##2.Subtraction
##3.Division
##4.Multiplication
##Enter your choice: 3
##Enter first number30
##Enter second number10
##Division of 30,10 is 3
