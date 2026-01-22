This repository contains basics as well the as advance concepts of python followed by concept of OOPS, data structure with implementation. 

Topics covered 
1) input and output in python
2) Variables and data types
3) Conditional expressions 
4) 


======================================================= Notes and Summary =======================================================

- How to install python libraries 
    Using keyword 'pip' + 'install' + 'name of the library' in the terminal

- how to take input and generate output ?
    for output using keyword 'print()' and for input we use var=input('')

- how to make comments in the code file ? 
    single line comments can be made using #comment goes here, 
    multi line comments using -> """ comment goes here """

- Variables and their types?
    variables can be intergers, boolea, float, long, string etc. They are used to store data and to perform operations on them. 
    variable names can have number, alphabets and undersocre but the name cannot start with a number and it cannot have whitespaces 

- operators in python ? 
    Arithmetic operators +,-,*,/
    assignement operator =, +=, -=,
    comparison operators ==,>,>=,<,<=,!=
    logical operators and, or , not 
    
- strings in python? 
    Immutable data type.all inputs by default are stored as string unless input is taken explicitly. Python supports string slicing with both positive and negative indexing. If we are counting from the front the index starts from 0. if we are counting from the back it starts from -1.
    
- List / arrays in python ?
    Python does not have arrays like c++/java do. python has lists which are also used as arrays. they are mutable data type in which we can store different types of data together. They have support of indexing start from 0 to length and support slicing just like strings do. 
 
- tuples ?
    tuples are datatypes which are immutable and can store multiple different types of data together. It also supports indexing and by concatination we can join 2 tuples

- Dictionary
    it is a set of key value pairs which is stored together, advantage of dictionary is that lookup is very fast. it is unordered, mutable, indexed and it cannot have duplicate keys.

- Sets ?
    collection of non repetitive elements. sets are unordered, unindexed and there is no way of changing the items in sets and cant have duplicate items in them. All elements inside a set are immutable and hashable.

- Conditional expressions and LOOPS 
    conditions which decide which part of the code is to be executed and which part is not to be executed.
    Types = IF - ELSE , ELIF ladder 
    Loops = For, While 

- Functions and recursions ?
    Function call ->
    Function definition -> 
    Types of Functions -> built in, User defined 

- File Manuplaton and operations?
    Performing operations such as read-write or input-output on a file.
    2 types of files -> text files and binary files 
    functions = 
        1) open(file_name, mode ) used to open a file by default in read mode 
        Common file modes
                Mode	Meaning
                "r"	Read (default)
                "w"	Write (creates or overwrites)
                "a"	Append
                "x"	Create new file
                "rb"	read in Binary mode
                "rt"	read in Text mode (default)
                "+" open for updating 
        2) file alias.read() used to read what is stored in the file
        3) file alias.close() used to close the file important to release      the system resources 
        4) file alias.write(string) used to write in the file 
        Best way to perform operations on files is to 
            {
                open with ("filename","mode") as f:
                    operations
            }
            because then you dont have to manually perform close operation  

----- OBJECT ORIENTED PROGRAMMING ----
Way of writting code by modeling it around real world objects instead of just using functions and logic 
    Basic definations 
        -> Classes -> blueprint/definition for creating objects 
        -> Objects -> combination of data (what it has) and behavior (what it does)
    
    What does it improve for us?

    Encapsulation
        Bundling data and methods together to restrict access
    Abstraction
        Shows what the object does but hides how it does it 
    Inheritance
        allows one class (child class) to inherit properties from another class (parent class)
    Polymorphism   
        Allows creations of methods with same name but different functioning. 
    
When a class is created a template is defined and then when object is created space in the memory is allocated 