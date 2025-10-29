#153
#1
#5
#3

#1234 ->4 3 2 1
#1234 -> 1 2 3 4

#division by 10 and extract reminder - %
#Pass quotient as input for next iteration

#n=int(input("Enter n"))
n=1234
numbers=[]

while(n>0):
    rem=n%10
    print(rem)
    numbers.append(rem)
    n=n//10

print(numbers)
numbers.sort(reverse=False)
print(numbers)

for i in numbers:
    print(i)


