f=open("learnings\dummy_text_file.txt")
data = f.read()
print(data)
f.close()

# write mode will write over the pre-existing text in the text file so to solve this we use append mode 
f=open("learnings\dummy_text_file.txt","w")
st="Write function helps us to write into the file and store it"
f.write(st)
f.close()

f=open("learnings\dummy_text_file.txt","a")
f.write("\n this does not overwrite pre-existing text instead appends the new line after the pre-existing text")
f.close()

f=open("learnings\dummy_text_file.txt")
lines=f.readline()
print(lines, type(lines))



''' if we dont want to write close statement again and again we can also do this 
with open("file_name) as alias:
    print(alias.function())
'''