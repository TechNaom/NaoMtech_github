#len()
s1="naomtech"

#2 scenarios
lenth1=len(s1)
print(f"The length is - {lenth1}")

#custom logic
count=0
for ch in s1:
    count+=1

print(f"The count is - {count}")
for i in range(lenth1-1,-1,-1):
    print(s1[i])

s2=""
for i in range(lenth1-1,-1,-1):
     s2=s2+s1[i]
print(f"The reversed string  is - {s2}")

s3=s1[::-1]
print(f"The reversed string  is - {s3}")

#upper()
#lower()
#swapcase

name1="HaryyPotter"
print(f"The lower of name is - {name1.lower()}")

name2="HaryyPotter"
print(f"The upper of name is - {name2.upper()}")

name3="HaryyPotter"
print(f"The swapcase of name is - {name2.swapcase()}")

#find vs index
name4="HaryyPotter"
print(f"The index  of P is - {name4.find('P')}")
print(name4[name4.find('P'):])

print(f"The index  of P is - {name4.index('P')}")
print(f"The index  of m is - {name4.find('m')}") #ValueError
#print(f"The index  of m is - {name4.index('m')}") #ValueError

#split()- splits a string into tokens
name5="John Peter Samson"
tokens_list=name5.split(" ") #retruns list
print(tokens_list)

for token in tokens_list:
    print(token)






















