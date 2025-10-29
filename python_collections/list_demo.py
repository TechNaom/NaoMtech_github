#List collection
'''
mutuble/immutable-->Mutuble
dynamic->yes
insertion order is preserved-->yes
duplicates-->yes
heterogenous/homogenous-->heterogenous
'''
from python_string_handling.string_intro import fruit

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

#concatenation of list
list3=list2+[10,20,30]
print(f"The new list is {list3}")

lst=[1,2]
print(lst * 5)

#slicing
integer_list=[1,2,3,4,1,2,3,4,"abc","xyz","aaa"]
print(integer_list[0:4]) #[1,2,3,4]
print(integer_list.index("abc")) #
print(integer_list[8:])

data_list=[1,2,3,4,"abc","xyz","aaa",10,20,30]
index1=data_list.index("abc") #
index2=data_list.index("aaa") #
print(index1)
print(index2)
print(data_list[index1:index2+1])

#Mutuble
fruits = ["apple", "banana", "cherry"]
fruits[0]="orange"
print(fruits)
fruits.append("Apple")
print(fruits)

























