##Q1.program to find sum of elements in list

##li=[10,20,30,40,50,60,70]
##sum1=0
##for i in li:
##    sum1=sum1+i
##print(f"sum of elements in list is:{sum1}")
##output
##sum of elements in list is:280

##Q2.to multiple elements of list

##li=[10,20,30,40,50,60,70]
##multi=1
##for i in li:
##    multi=multi*i
##print(f"multiplication of elements in list is:{multi}")
##output
##multiplication of elements
##in list is:50400000000

##Q3.program to find smallest number in list

##li=[5,8,4,6,8,9]
##sml=li[1]
##for i in li:
##    if sml<i:
##        pass
##    else:
##        sml=i
##print("smallest number is:",sml)
##output
##smallest number is: 4
    
##Q4.program to find largest number in list

##li=[5,8,4,6,8,9]
##l=li[1]
##for i in li:
##    if l>i:
##        pass
##    else:
##        l=i
##print("largest number is:",l)
##output
##largest number is: 9

##Q5find second highest number

##list1 = [10, 20, 40,50]
## 
##mx = max(list1[0], list1[1]) 
##secondmax = min(list1[0], list1[1]) 
##n = len(list1)
##for i in range(2,n): 
##    if list1[i] > mx: 
##        secondmax = mx
##        mx = list1[i] 
##    elif list1[i] > secondmax and \
##        mx != list1[i]: 
##        secondmax = list1[i]
##    elif mx == secondmax and \
##        secondmax != list1[i]:
##          secondmax = list1[i]
## 
##print("Second highest number is : ",\
##      str(secondmax))
##output:
##    Second highest number is :  40

##Q6.find N largest element from list

##def Nmaxelements(list1, N):
##    final_list = []
## 
##    for i in range(0, N):
##        max1 = 0
## 
##        for j in range(len(list1)):
##            if list1[j] > max1:
##                max1 = list1[j]
## 
##        list1.remove(max1)
##        final_list.append(max1)
## 
##    print(f"{N} largest elements are:",final_list)
## 
##list1 = [20, 60, 41, 85,30, 70, 60, 10]
##N = 2
## 
##Nmaxelements(list1, N)
##output
##2 largest elements are: [85, 70]

##Q7.print even numbers in list

##li=[]
##for i in range(1,21):
##    if i%2==0:
##        li.append(i)
##print(f"Even numbers from 1 to 20 are:",li)
##output
##Even numbers from 1 to 20 are:
##[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

##Q8.print odd numbers in list

##li=[]
##for i in range(1,21):
##    if i%2!=0:
##        li.append(i)
##print(f"Odd numbers from 1 to 20 are:",li)
##output
##Odd numbers from 1 to 20 are:
##[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

##Q9.Remove empty list from list

##def empty_list_remove(input_list):
##    new_list = []
##    for ele in input_list:
##        if ele:
##            new_list.append(ele)
##    return new_list
##
##input_list = [5, 6, [], 3, [], [], 9]
##print(f"The original list is : {input_list}")
##print(f"List after empty list removal :"\
##      f"{empty_list_remove(input_list)}")
##output:
##The original list is : [5, 6, [], 3, [], [], 9]
##List after empty list removal :[5, 6, 3, 9]

##Q10.program to cloning or copying a list

##lst = [4, 8, 2, 10, 15, 18]
##li_copy =list(map(int, lst))
##print("Original List:", lst)
##print("After Cloning:", li_copy)
##output
##Original List: [4, 8, 2, 10, 15, 18]
##After Cloning: [4, 8, 2, 10, 15, 18]

##Q11.program to count occurence of an element in a list

##li=[2,2,5,4,6,7,4,3,5,2,5,2,3]
##for i in li:
##    count=0
##    for j in range(len(li)):
##        if i==li[j]:
##            count+=1
##    print(f"occcurance of number"\
##          f" {i} is:",count)
##output
##occcurance of number 2 is: 4
##occcurance of number 2 is: 4
##occcurance of number 5 is: 3
##occcurance of number 4 is: 2
##occcurance of number 6 is: 1
##occcurance of number 7 is: 1
##occcurance of number 4 is: 2
##occcurance of number 3 is: 2
##occcurance of number 5 is: 3
##occcurance of number 2 is: 4
##occcurance of number 5 is: 3
##occcurance of number 2 is: 4
##occcurance of number 3 is: 2
