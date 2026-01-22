class emp:
    language="py"

    def getinfo(self):
        print(f"emp's language is:{self.language}")
    
    @staticmethod 
    def greet():
        print("Good morning")
a=emp()
a.getinfo()
a.greet()
# why do we use self?
'''
    a.getinfo() is interpreted as emp.getinfo(a),
    so it takes an argument.
    Hence, we use self to receive that object.
    
    In case we dont want the function to need object then we can create a static methods/function 
'''
