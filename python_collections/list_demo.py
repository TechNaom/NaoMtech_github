#List collection
'''
mutuble/immutable-->Mutuble
dynamic->yes
insertion order is preserved-->yes
duplicates-->yes
heterogenous/homogenous-->heterogenous
'''

list1=[1,2,3,4,5,"123",True,10+20j] #Heterogenous
print(list1)

list1[0]=100
print(list1)

print(len(list1))
list1.append(1000) #Adding value to a list
print(list1)

list2=[1,2,3,1,2,3]
print(list2)

#Reading values from list
#indexing
#Iterating - for
print(list2[0]) #1
print(list2[1]) #2
print(list2[2]) #3

#Iterating list
for value in list1:
    print(value)









