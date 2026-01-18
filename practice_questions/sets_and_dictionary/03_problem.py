# create an empty dictionary and also allow 4 friends to inpout names and values in it 

dict = {}

for i in range(0,4):
    name= input("enter your name: ")
    lang = input("enter your language: ")
    dict.update({name: lang})

print(dict)