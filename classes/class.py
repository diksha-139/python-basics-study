class student:
    course ="python"
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display(self,address):
        self.address=address
        print("I am {},{}years old and live in {}".format(self.name,self.age,self.address))
p1 = student("diksha",28)
p1.display("kochi")