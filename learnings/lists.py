list1 = [1,2.2, "String", "Hello"]

print(list1[1])
print(list1[:3])

# methods in lists causes changes to the actual list unline in case of strings that create a copy 

list1.append("new")
print(list1)
list1.insert(1, 5) # inserts at index 1, value 5 
print(list1)
list1.pop(2) # removes and returns element at index 2; if no value then removes and returns the last element 
# list1.sort() sorts the list but not possible when we have strings as it relies on < operator 
print(list1)
list1.remove("String")
list1.remove("Hello")
print(list1)