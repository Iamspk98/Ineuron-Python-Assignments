##Q1.program to find sum of array

##lenght=int(input("enter lenght of array"))
##li=list()
##for i in range(lenght):
##    elmnt=int(input("enter element:"))
##    li.append(elmnt)
##
##print(li)
##sum1=0
##for i in range(lenght):
##    sum1=sum1+li[i]
##
##print("sum of array is :",sum1)
##output
##enter lenght of array5
##enter element:1
##enter element:2
##enter element:3
##enter element:4
##enter element:5
##[1, 2, 3, 4, 5]
##sum of array is : 15

##Q2.to find largest element in an array

##lenght=int(input("enter lenght of array:"))
##li=list()
##for i in range(lenght):
##    elmnt=int(input("enter element:"))
##    li.append(elmnt)
##print(li)
##lrg=0
##for i in range(lenght):
##    if lrg<li[i]:
##        lrg=li[i]
##    else:
##        pass
##
##print("largest element is :",lrg)
##output
##enter lenght of array:5
##enter element:9
##enter element:8
##enter element:7
##enter element:6
##enter element:5
##[9, 8, 7, 6, 5]
##largest element is : 9

##Q3.program for array rotation
##
##lenght=int(input("enter lenght of array:"))
##li=list()
##for i in range(lenght):
##    elmnt=int(input("enter element:"))
##    li.append(elmnt)
##print(li)
##rtt=0
##for i in range(lenght//2):
##    rtt=li[i]
##    if i==0:
##        li[i]=li[lenght-1]
##        li[lenght-1]=rtt
##        
##    else:
##        li[i]=li[lenght-(i+1)]
##        li[lenght-(i+1)]=rtt
## 
##print("rotated array is :",li)
##output
##enter lenght of array:5
##enter element:1
##enter element:2
##enter element:3
##enter element:4
##enter element:5
##[1, 2, 3, 4, 5]
##rotated array is : [5, 4, 3, 2, 1]

##Q4.split array and add first part at the end
##
##lenght=int(input("enter lenght of array:"))
##li=list()
##li2=list()
##for i in range(lenght):
##    elmnt=int(input("enter element:"))
##    li.append(elmnt)
##print(li)
##rtt=0
##for i in range(lenght//2):
##    li2.append(li[i])
##    li.append(li2[i])
##    
##for i in range(lenght//2):
##    li.remove(li[0])
##
##print("Splited list is :",li)
##output
##enter lenght of array:5
##enter element:1
##enter element:2
##enter element:3
##enter element:4
##enter element:5
##[1, 2, 3, 4, 5]
##Splited list is : [3, 4, 5, 1, 2]

##Q5.check given array is monotonic

##def isMonotonic(A):
##    return (all(A[i]<=A[i+1] for i in range(len(A)-1)) or
##           (all(A[i]>=A[i+1] for i in range(len(A)-1))))
##
##A=[6,5,4,4]
##print(isMonotonic(A))
##output
##True
