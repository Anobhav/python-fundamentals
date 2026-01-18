# python function to remove a given word from the list and strip it at the same time 

lista=["Ano","bha", "v","sin", "gh"]
for i in range(len(lista)):
    lista[i] = lista[i].strip()
print(lista)

def check(a):
    a=a.strip()
    found=False
    for i in range(0, len(lista)):
        if(lista[i]==a):
            print("word found now removing")
            lista.pop(i)
            found=True
            break
    if not found:
        print("word is not found it does not exists in the list")
def enter():
    a=input("enter the word you want to remove: ")
    check(a)

enter()