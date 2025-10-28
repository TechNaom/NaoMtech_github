string1="Bitty"
string2="Putty"

#Case1
string3=string1+string2
print(f"The result   of string3 - {string3}")  #
print(f"The result  of sum - {10+20}")  #

string4="abc"+str(4)
print(f"The result   of string4 - {string4}")  #

print('abc'*3)

paths=["/abc/bbc/bbc",'xxx/yyy/abc','ddd/aaa/xxx']

print('abc' in paths)#False

for path in paths:
    if("abc" in path):
        print(f"{'abc'} is found in {path}")

paths2=["abc",'xxx','aaa']
print('abc' in paths2)#True

if "xyz" not in paths2:
    print(f"{'xyz'} is not found in {paths2}")

#Format specifiers
name="abc" #%s
age=30 #%d
sal=2000.00 #%f

print("%s %d %f "%(name,age,sal))

#format()
name="John"
age=40

print("The name is {} and age is {}".format(name,age))
print("The age is {1} and name is {0}".format(name,age))

#Join method
s="abc"
s2='and'
print(s2.join(s))


formatted_string=' ' .join(['the', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog'])
print(formatted_string)















