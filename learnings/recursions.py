#solving the problem of calculating factorial with the help of factorial 

def factorial(n):
    if (n==0 or n==1):
        return 1
    else :
        return n*factorial(n-1)





n=int(input("enter the number for which we need to calculate the factorial: "))
print(factorial(n)) 