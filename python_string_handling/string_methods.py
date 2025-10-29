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
tokens_list=name5.split(" ") #returns list
print(tokens_list)

for token in tokens_list:
    print(token)

string1=" Naom "
print(len(string1))
string2=string1.lstrip()
print(f"The lstrip()  of {string1} is - {string2}") #ValueError
print(len(string2))
string3=string1.rstrip()
print(f"The rstrip()  of {string3} is - {string3}") #ValueError
print(len(string3))
string4=string1.strip()
print(f"The strip()  of {string4} is - {string4}") #ValueError
print(len(string4))

pattern1="abc123"
print(f"The  isalnum  of {pattern1} is - {pattern1.isalnum()}") #True
print(f"The  isalpha  of {pattern1} is - {pattern1.isalpha()}") #False
print(f"The  isdigit  of {pattern1} is - {pattern1.isdigit()}") #False
print(f"The  islower  of {pattern1} is - {pattern1.islower()}") #True
print(f"The  isupper  of {pattern1} is - {pattern1.isupper()}") #False
print(f"The  isspace  of {pattern1} is - {pattern1.isspace()}") #False

#max method
print(f"The  max  of {pattern1} is - {max(pattern1)}") #c

#min method
print(f"The  min  of {pattern1} is - {min(pattern1)}") #1

#/abc/xyz/bbc/2025-10-27
path="/abc/xyz/bbc"

if path.startswith("/abc/xyz"):
    print(f"The path  of {path} is found - {path}")  #
    pass

if path.endswith("/bbc"):
    print(f"The path  of {path} is found - {path}")  #
    pass

pattern2="Apple"
print(pattern2.replace('A','B'))







































