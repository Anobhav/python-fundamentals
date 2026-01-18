# recursive function to calculate the sum of first n natural numbers 
def find_sum(n):
    if (n<=1):
        return n
    else:
        return (n+find_sum(n-1))

n=int(input("enter the number for which you want them sum: "))
print(find_sum(n))