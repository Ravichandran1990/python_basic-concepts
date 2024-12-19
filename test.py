class Parent:
    def __init__(self):
        self.parent_price = 4000

    def display(self):
        print(f"This is parent display price {self.price + self.parent_price}")
class Child(Parent):
    def __init__(self):
        super().__init__()
        self.price = 5000

child = Child()
child.display()
