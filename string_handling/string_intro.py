   #01234567
s1='NaomTech'
   #-8-7-6....
#Extracting characters using index
print(s1[0]) #N
print(s1[3]) #m
print(s1[-1]) #h
print(s1[-2]) #c

#way2
#Iteration
#Iterating a string char by char
for char in s1:
    print(char)

#way-3 -slicing
print(s1[0:4])
print(s1[:4])
print(s1[4:8])
print(s1[4:])
print(s1[3:5])
print(s1[::-1])
print(s1[::-2])
print(s1[0::2])

name="Amitab Bacchan"
print(name)
print(name[0:6])
print(name[0:-3])
print(name[-1:-8])
print(name[1:-8])
print(name[1:-1])
print(name[2:1])
print("Test",name[-1:6]) #


singers = "Peter, Paul, and Mary"
print(singers[0:5])
print(singers[7:11])
print(singers[17:21])

fruit = "banana"
print(fruit[:])
print(fruit[:4])
print(fruit[4:])

filename1 ="abcdef2024-12-12"
filename2 ="2024-12-12abcdef"
filename3 ="abcdef2024-12-12sdskdjksdjskj"

print(filename1[6:])
print(filename2[:10])
print(filename3[6:16])

print(fruit[::-1])






























