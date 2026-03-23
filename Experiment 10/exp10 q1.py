class parent:
    def display(self):
        print("This is parent class")
class child(parent):
    def show(self):
        print("This is child class")
c = child()
p = parent()
p.display() 
c.display()  
c.show()    
