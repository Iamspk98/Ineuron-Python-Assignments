##Q1
##def matrix(m,n):
##    o=[]
##    for i in range(m):
##        row=[]
##        for j in range(n):
##            inp=int(input(f"enter o[{i}][{j}]"))
##            row.append(inp)
##        o.append(row)
##    return o
##def sum1(A,B):
##    output=[]
##    for i in range(len(A)):
##        row=[]
##        for j in range(len(A[0])):
##            row.append(A[i][j]+B[i][j])
##        output.append(row)
##    return output
##m=int(input("enter the value of m"))
##n=int(input("enter the value of n"))
##
##print("enter matrix A")
##A=matrix(m,n)
##print(A)
##
##print("enter matrix B")
##B=matrix(m,n)
##print(B)
##
##O=sum1(A,B)
##print("sum ofMatrix\n",O)
##output
##enter the value of m2
##enter the value of n2
##enter matrix A
##enter o[0][0]1
##enter o[0][1]2
##enter o[1][0]3
##enter o[1][1]4
##[[1, 2], [3, 4]]
##enter matrix B
##enter o[0][0]5
##enter o[0][1]6
##enter o[1][0]7
##enter o[1][1]8
##[[5, 6], [7, 8]]
##sum ofMatrix
## [[6, 8], [10, 12]]

##Q2.multiply two matrix
##
##def matrix(m,n):
##    o=[]
##    for i in range(m):
##        row=[]
##        for j in range(n):
##            inp=int(input(f"enter o[{i}][{j}]"))
##            row.append(inp)
##        o.append(row)
##    return o
##def mul1(A,B):
##    output=[]
##    for i in range(len(A)):
##        row=[]
##        for j in range(len(A[0])):
##            row.append(A[i][j]*B[i][j])
##        output.append(row)
##    return output
##m=int(input("enter the value of m"))
##n=int(input("enter the value of n"))
##
##print("enter matrix A")
##A=matrix(m,n)
##print(A)
##
##print("enter matrix B")
##B=matrix(m,n)
##print(B)
##
##O=mul1(A,B)
##print("multiplication of Matrix\n",O)
##output
##enter the value of m2
##enter the value of n2
##enter matrix A
##enter o[0][0]1
##enter o[0][1]2
##enter o[1][0]3
##enter o[1][1]4
##[[1, 2], [3, 4]]
##enter matrix B
##enter o[0][0]5
##enter o[0][1]6
##enter o[1][0]7
##enter o[1][1]8
##[[5, 6], [7, 8]]
##multiplication of Matrix
## [[5, 12], [21, 32]]

##Q3.transpose a matrix

##def insert(m,n):
##    o=[]
##    for i in range(m):
##        row=[]
##        for j in range(n):
##            inp=int(input(f"enter o[{i}][{j}]"))
##            row.append(inp)
##        o.append(row)
##    return o
##
##def transpose(A,B):
##    global m,n
##    for i in range(m):
##        for j in range(n):
##            B[i][j]=A[j][i]
##    return B
##            
##m=int(input("Enter the value of m:"))
##n=int(input("Enter the value of n:"))
##
##A=insert(m,n)
##print(A)
##B=A[:][:]
##T=transpose(A,B)
##print(T)
##output
##Enter the value of m:3
##Enter the value of n:3
##enter o[0][0]7
##enter o[0][1]8
##enter o[0][2]9
##enter o[1][0]4
##enter o[1][1]5
##enter o[1][2]6
##enter o[2][0]1
##enter o[2][1]2
##enter o[2][2]3
##[[7, 8, 9], [4, 5, 6], [1, 2, 3]]
##[[7, 4, 1], [4, 5, 2], [1, 2, 3]]

##Q4.python program to sort words in Alphabetical Order

##str1=input("Enter the String:")
##words=[word.lower()for word in str1.split()]
##
##words.sort()
##print("The sorted words are:")
##
##for word in words:
##    print(word)
##output
##Enter the String:hii how are you
##The sorted words are:
##are
##hii
##how
##you

##Q5.remove punctuation from a string

##punctuations='''!@#$%^&*()_-'"|\?:;~?/{}[]<>.,'''
##
##str1=input("enter a String:")
##
##no_punct=""
##
##for char in str1:
##    if char not in punctuations:
##        no_punct=no_punct+char
##
##print(no_punct)
##output
##enter a String:hello ,how are you?
##hello how are you
