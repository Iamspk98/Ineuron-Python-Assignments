#Q1.to find words which are greater than given length k

#inp=input("Enter the String:")
#k=5
#condition to compare length of String
#if len(inp)>k:
#    print("Length of String is greater than K")
#else:
#    print("Length of String is less than K")

#output
#Enter the String:adam
#Length of String is less than K

#Q2.program for removing i-th character from a string

#inp=input("Enter the String:")
#char=""
#pos=3
#i=0
#print(f"Before removing of i-th charactrer string is:{inp}")

#for j in inp:
#    if i!=pos:
#        char=char+j
#    else:
#        pass
#    i+=1
#print(f"After removal of i-thcharacter string is:{char}")

#output
#Enter the String:anant
#Before removing of i-th charactrer string is:anant
#After removal of i-thcharacter string is:anat

#Q3.program to split and join a string

#string=input("Enter the string:")

#def split_str(string):
#    list_str=string.split(' ')
#    return list_str

#def join_str(list_str):
#    joined_str='-'.join(list_str)
#    return joined_str

#list_str=split_str(string)
#print(list_str)

#new_str=join_str(list_str)
#print(new_str)

#output
#Enter the string:heloo how are you
#['heloo', 'how', 'are', 'you']
#heloo-how-are-you

#Q4.to check given string is binary string or not

#string=input("Enter the string:")
#set1=set(string)
#set2={'0','1'}
#if set1==set2 or set1=={'0'} or set1=={'1'}:
#    print("String is Binary string")
#else:
#    print("String is NoT Binary String")

#output
#Enter the string:010101
#String is Binary string

#Q5.pythonprogram to find uncommon words from two strings

#str1=input("Enter the first string:")
#str2=input("Enter Seocnd String:")
#lst3=[]
#def split_str(strr):
#    list1=strr.split()
#    return list1

#def join_str(lst):
#    str3=','.join(lst)
#    return str3
#lst1=split_str(str1)
#lst2=split_str(str2)

#for i in lst1:
#    if i not in lst2:
#        lst3.append(i)

#for i in lst2:
#    if i not in lst1:
#        lst3.append(i)

#str3=join_str(lst3)
#print(f"uncommon words are:{str3}")

#output
#Enter the first string:hello how are you
#Enter Seocnd String:what are you doing
#uncommon words are:hello,how,what,doing

#Q6.find  all duplicate character in string

#def duplicate_characters(string):

#    chars = {}


#    for char in string:

#        if char not in chars:
#            chars[char] = 1
#        else:

#            chars[char] += 1

#    duplicates = []

#    for char, count in chars.items():
#        if count > 1:
#            duplicates.append(char)

#    return duplicates

#string=input("Enter the String:")
#print(duplicate_characters(string))

#output
#Enter the String:anant
#['a', 'n']

#Q7.progaram to check if a string contains any special character

#spl_chr='[@_!$%^&*()<>?/\\|}{~:]#'
#str1=input("Enter String")
#count=0
#for i in str1:
#    if i in spl_chr:
#        count=1

#if count==1:
#    print("String contain special character")
#else:
#    print("String Does not contain any special character")

#output
#Enter Stringaf456@#
#String contain special character
