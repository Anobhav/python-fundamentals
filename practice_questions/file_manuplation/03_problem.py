# generate 2 files with the table fo 2 and 3 and place it them in a folder 

with open("practice_questions\\file_manuplation\\03_problem1.txt","w")as f:
    i=1
    while(i<=10):
        f.write(f"{i} * 2={i*2}\n")
        i+=1
with open("practice_questions\\file_manuplation\\03_problem2.txt","w")as f:
    i=1
    while(i<=10):
        f.write(f"{i} * 3={i*3}\n")
        i+=1