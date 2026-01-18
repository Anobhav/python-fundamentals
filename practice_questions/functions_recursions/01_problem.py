# find greatest of 3 numbers 

def greatest(a,b,c):
    if a>=b and a>=c:
        print(f"{a} is the greatest")
    elif b>=a and b>=c:
        print(f"{b} is the greatest")
    else:
        print(f"{c} is the greatest")

def enter():
    a=int(input("enter the 1st number"))
    b=int(input("enter the 2nd number"))    
    c=int(input("enter the 3rd number"))
    greatest(a,b,c)

enter()
