# take input from user and display all the unique ones 
i=0
nums = set()
count = int(input("enter the numbers you want to store:"))
while(i<count):
    n=int(input("enter the number:"))
    nums.add(n)
    i=i+1

print(nums)