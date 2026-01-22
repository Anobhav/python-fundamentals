# wirte a program to read the text froma file called poems.txt and find out if it contains the word twinkle 

with open("practice_questions\\file_manuplation\\poems.txt") as f:
    content = f.read()
    if "Twinkle" in content:
        print("Twinkle is found")
    else:
        print("Twinkle is not found")
