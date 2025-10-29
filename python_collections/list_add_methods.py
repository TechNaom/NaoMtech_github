#Validating list and craeting sublists - Use append

list1=[1,"abc",2,3,4,12.35,"xyz","bbc",8.36,2.21]

#Empty lists
int_list=[]
string_list=[]
float_list=[]

#Iterating list
for value in list1:
    if type(value)==int:
        int_list.append(value)
    elif type(value)==str:
        string_list.append(value)
    else:
        float_list.append(value)

print(f"int_list - {int_list}")
print(f"string_list - {string_list}")
print(f"float_list - {float_list}")

#insert
#insert value at a given position
print(list1)
list1.insert(2,1000)
print(list1)

list2=[10,20,30]
list1.append(list2) #
print(list1)

list3=[10,20,30]
list1.extend(list3) #Flattening
print(list1)

#Removing elements
fruits = ["apple", "banana", "cherry", "orange"]
print(fruits)
#remove()
fruits.remove("orange") #
print(fruits)

#fruits.remove("orange") #ValueError
#print(fruits)
#pop
fruits.pop(2) #Cherry is gone #IndexError
print(fruits)

#Final check

#del
del fruits[1]
print(fruits)

del fruits[0]
print(fruits) #Empty list

del fruits
print(fruits) #Empty list






