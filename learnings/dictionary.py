empty_dict = {}
marks = {
    "Ano":100,
    "Shu" : 56,
    "List": ["a","b","c","d","e"]
}

print(marks["List"])
print( type(marks))
print(marks["Shu"])

# dictionary methods 

print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"Ano":90, "Ren":55})
print(marks)
print(marks.get("ano"))