l1 = [1,2,3,4,5,6,7,8,9]

print("using for loop")
for i in range(8): # 0 to 7 
    print(l1[i])

print("using while loop")
j=0
while(j<len(l1)): # 0 to 8 
    print(l1[j])
    j+=1

l=["this", "is", "a", "list"]
t=("this", "is", "a", "tuple")
s="anobhav"

for i in l:
    print(i)
    if(i =="a"):
        break # exit the loop 
else:
    print("list printed \n")

for i in t:
    print(i)
else:
    print("tuple printed \n")
for i in s:
    if(i=="v"):
        continue
    print(i)
else:
    print("string printed \n")

#range(start, stop, step size) 
for i in range(0, len(l), 2):
    print(l[i])
for i in range(0, len(t), 2):
    print(t[i])
for i in range(0, len(s), 2):
    pass # do nothing 
