# data = {'name': 'Ravichandran', 'lname': 'Mohan'}
# print(len(data))


#dictionary function call without if and switch case
def a():
    print("a")
def b():
    print("b")
def c():
    print("c")
def d():
    print("d")
    
def default():
    print("default")
    
option = "e"
    
f = {"a": a, "b":b,"c":c,"d":d, "default": default}
f.get(option, default)()