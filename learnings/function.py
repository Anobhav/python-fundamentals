# program to cal avg using function 

def avg(a,b,c):
    avg=(a+b+c)/3
    return avg

def enter_by_user():
    a=int(input("enter 1st num"))
    c=int(input("enter 2st num"))
    b=int(input("enter 3st num"))
    ans=avg(a,b,c)
    return ans

print(enter_by_user())


# passing arguments and functions 

def goodday(name, ending="Thank you"):
    print(f"Good day {name}")
    print(ending)

goodday("anobhav", "Thank you")
goodday("Sim")
