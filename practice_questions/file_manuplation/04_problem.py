with open("practice_questions\\file_manuplation\\04_problem.txt","r") as f:
    content = f.read()
    
lista=["donky","Donky"]
for word in lista:
    content=content.replace(word,"#####")
with open("practice_questions\\file_manuplation\\04_problem.txt","w") as f:
    f.write(content)