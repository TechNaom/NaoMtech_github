#/  - Quotient float division
# // - quotient int division
# %  - Reminder

a=10
b=5

print(a/b)
print(a//b)

print(b//a)
print(b/a)

print(a%b)
print(b%a)

print(a+b)
print(a-b)
print(a*b)
print(a**2)

#Addition of 2 numbers

#Inputs
#reading a
a=int(input("Enter a"))
b=int(input("Enter b"))

#Logic building
c=a+b

#Printing
print("The sum of",a,"and",b,"is",c)
print("The sum of {} and {}  is {}".format(a,b,c))
print(f"The sum of {a} and {b}  is {c}")

a=10

#increment by 2
a=a+2
print(a)
a=a-2
print(a)

#short hand
a+=2  #a=a+2
print(a) #12
a-=2  #a=a+2
print(a) #10
a*=2  #a=a+2
print(a) #20

fruits=["apple","orange","banana"]

print("apple" in fruits)
print("jackfruit" in fruits)
print("jackfruit" not in fruits)



a=10
b=5

print(a>b) #True
print(a<b) #False
print(a>=b) #True
print(a<=b) #False
print(a==b) #False
print(a!=b) #True

