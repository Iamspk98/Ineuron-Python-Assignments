##Q1.program to check Disarium number
##def is_disarium(num):
##    temp = 0
##    for i in range(len(str(num))):
##        temp += int(str(num)[i]) ** (i + 1)
##    return temp == num
##
##num =int(input("Enter a Number:"))
##print("Is",num," Disarium number?",is_disarium(num))
##output
##Enter a Number:175
##Is 175  Disarium number? True

##Q2.print disarium number betwwen 1 to 100

##def is_disarium(num):
##    temp = 0
##    for num in range(101):
##        
##        for i in range(len(str(num))):
##            temp += int(str(num)[i]) ** (i + 1)
##            if temp == num:
##                print(f"{num} is Disarium")
##            else:
##                pass
##num=0
##is_disarium(num)
####num =int(input("Enter a Number:"))
####print("Is",num," Disarium number?",is_disarium(num))
##output
##0 is Disarium
##1 is Disarium

##Q3.checknumber is happy number

##def squaredsum(num):
##    sum = 0
##    while(num):
##        sum += (num%10) ** 2
##        num = num//10
##    return sum
##
##def happynumber(num):
##    record  = set()
##    while(1):
##        num = squaredsum(num)
##        if num==1:
##            return True
##        if num in record:
##            return False
##        record.add(num)
##
##num = int(input("Enter a number: "))
##if happynumber(num):
##    print(num,"is a happy Number")
##else:
##    print(num,"is not a happy number")
##
##output    
##Enter a number: 19
##19 is a happy Number

##Q4.print all happy numbers 1  to 100

##def squaredsum(num):
##    sum = 0
##    while(num):
##        sum += (num%10) ** 2
##        num = num//10
##    return sum
##
##def happynumber(num):
##    record  = set()
##    while(1):
##        num = squaredsum(num)
##        if num==1:
##            return True
##        if num in record:
##            return False
##        record.add(num)
##
####num = int(input("Enter a number: "))
##for num in range(101):        
##    if happynumber(num):
##        print(num,"is a happy Number")
##    else:
##        pass
##output
##1 is a happy Number
##7 is a happy Number
##10 is a happy Number
##13 is a happy Number
##19 is a happy Number
##23 is a happy Number
##28 is a happy Number
##31 is a happy Number
##32 is a happy Number
##44 is a happy Number
##49 is a happy Number
##68 is a happy Number
##70 is a happy Number
##79 is a happy Number
##82 is a happy Number
##86 is a happy Number
##91 is a happy Number
##94 is a happy Number
##97 is a happy Number
##100 is a happy Number

##Q5.check given number is Harshad Number

##def harshNumber(num):
##    sum1=rem=0
##    n=num
##    while(n>0):
##        sum1=sum1+(n%10)
##        n=n//10
##    if num%sum1==0:
##        return True
##    else:
##        return False
##
##num=int(input("Enter a Number:"))
##
##if harshNumber(num):
##    print(num,"is Harshad Number")
##else:
##    print(num,"is not Harshad Number")

##n=int(input("Enter a Number:"))
##p=n
##l=[]
##sum1=0
##while(n>0):
##    x=n%10
##    l.append(x)
##    n=n//10
##sum1=sum(l)
##if(p%sum1==0):
##    print("Harshad number")
##else:
##    print("Not harshad number")
##
##output
##Enter a Number:12
##12 is Harshad Number

##Q6.program to print all pronic no betn 1 to 100
##
##def isPronicNumber(num):    
##    flag = False   
##        
##    for j in range(1, num+1):    
##        #Checks for pronic number by multiplying consecutive numbers    
##        if((j*(j+1)) == num):    
##            flag = True   
##            break    
##    return flag    
##     
###Displays pronic numbers between 1 and 100    
##print("Pronic numbers between 1 and 100: ")    
##for i in range(1, 101):    
##    if(isPronicNumber(i)):    
##        print(i)   
##        print(" ")
##output
##Pronic numbers between 1 and 100: 
##2
## 
##6
## 
##12
## 
##20
## 
##30
## 
##42
## 
##56
## 
##72
## 
##90
