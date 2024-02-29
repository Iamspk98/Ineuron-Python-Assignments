#Q1.python program to extract unique values dictionary values

#dict1={'a':1,'b':2,'c':3,'d':3,'e':5,'f':6}
#i=0
#dict2={}
#print(dict1.values())
#for key,value in dict1.items():
#    if i!=0:
#        if value not in dict2.values():
#            dict2[key]=value
#        else:
#            pass
#    else:
#        dict2[key]=value
#    i+=1

#lst=dict2.values()
#print(f"unique values are {lst}")

#output
#dict_values([1, 2, 3, 3, 5, 6])
#unique values are dict_values([1, 2, 3, 5, 6])

#Q2.python program to find the sum of all values in a dictionary

#dict1={'a':1,'b':2,'c':3,'d':3,'e':5,'f':6}
#sum=0
#for value in dict1.values():
#    sum=sum+value

#print(f"sum of all values:{sum}")

#output
#sum of all values:20

#Q3. program to merging two dictionaries

#dict1={'ten':10,'twenty':20,'thirty':30}
#dict2={'thirty':30,'fourty':40,'fifty':50}

#dict1.update(dict2)
#print(dict1)

#output
#{'ten': 10, 'twenty': 20, 'thirty': 30, 'fourty': 40, 'fifty': 50}

#Q4. python program to convert key-values list to flat dictionary

#test_dict = {'month': [1, 2, 3],
#'name': ['Jan', 'Feb', 'March']}

#print("The original dictionary is : " + str(test_dict))

#x = list(test_dict.values())
#a = x[0]
#b = x[1]
#d = dict()
#for i in range(0, len(a)):
#    d[a[i]] = b[i]

#print("Flattened dictionary : " + str(d))

#output
#The original dictionary is : {'month': [1, 2, 3], 'name': ['Jan', 'Feb', 'March']}
#Flattened dictionary : {1: 'Jan', 2: 'Feb', 3: 'March'}

#Q5. python program to insertion at the beginning in OrderedDict

#from collections import OrderedDict

#ini_dict1 = OrderedDict([('akshat', '1'), ('nikhil', '2')])
#ini_dict2 = OrderedDict([("manjeet", '4'), ("akash", '4')])

#both = OrderedDict(list(ini_dict2.items()) + list(ini_dict1.items()))

#print("Resultant Dictionary :" + str(both))

#output
#Resultant Dictionary :OrderedDict({'manjeet': '4', 'akash': '4', 'akshat': '1', 'nikhil': '2'})

#Q6. python program to check order of character in string using OrderedDict()

#def check_order(string, pattern):
#    i, j = 0, 0
#    for char in string:
#        if char == pattern[j]:
#            j += 1
#        if j == len(pattern):
#            return True
#        i += 1

#    return False


#string = 'engineers rock'
#pattern = 'er'
#print(check_order(string, pattern))

#output
#True

#Q7. python program to sort python Dictionaries by key or value

#myDict = {'ravi': 10, 'rajnish': 9,
#          'sanjeev': 15, 'yash': 2, 'suraj': 32}

#myKeys = list(myDict.keys())
#myKeys.sort()
#sorted_dict = {i: myDict[i] for i in myKeys}

#print(sorted_dict)

#output
#{'rajnish': 9, 'ravi': 10, 'sanjeev': 15, 'suraj': 32, 'yash': 2}
