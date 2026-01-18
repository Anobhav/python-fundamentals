# factorial of a number 

n=int(input("enter the number for which you want to calculate the factorial"))
fact=n
while(n>1):
    fact=fact*(n-1)
    n-=1

print("factorial of n is:",fact)