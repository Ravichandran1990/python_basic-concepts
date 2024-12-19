class Parent:
    def __init__(self) -> None:
        self.price = 5000
    
    def display(self) -> None:
        print(f"Display price would be {self.price}")
        
class Child(Parent):
    def __init__(self) -> None:
        super().__init__()
        self.price = 6000
        
child = Child()
child.display()
        
        