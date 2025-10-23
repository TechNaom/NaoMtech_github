#Sum of first n natural numbers
#Sum of even natural numbers

#Initialization
i=1
n=int(input("enter n"))
result=0
while(i<=n):
    if(i%2==0):
        result=result+i
        print(f"The sum is {result}")
    i=i+1

print(f"The sum is {result}")


