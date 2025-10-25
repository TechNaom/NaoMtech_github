a=int(input("Enter a"))
b=int(input("Enter b"))
c=int(input("Enter c"))


#Validatation
if a>b:
    if a>c:
        print(f"{a} is bigger than {b} and {c}")

if b>a:
    if b>c:
        print(f"{b} is bigger than {a} and {c}")

if c>a:
    if c>b:
        print(f"{c} is bigger than {a} and {b}")
