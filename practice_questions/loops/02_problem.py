# print alll the names in a list 

l=["ano","sha", "ram", "jai"]

for i in range(len(l)):
    print(l[i])

# to print a specific name that starts witha speicfic letter 

for i in l:
    if(i.startswith("r")):
        print(i)

