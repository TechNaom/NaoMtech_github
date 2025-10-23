a=int(input("Enter a"))
b=int(input("Enter b"))
c=int(input("Enter c"))


if(a>b and a>c):
    print(f"{a} is bigger than {b} and {c}")
elif b>c:
    print(f"{b} is bigger than {a} and {c}")
else:
    print(f"{c} is bigger than {a} and {b}")