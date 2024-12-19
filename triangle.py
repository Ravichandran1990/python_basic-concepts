a = int(input("Enter a number"))
for i in range(1, (a+1)):
    findSpace = int((a - i) / 2)
    print(f"{findSpace * ' '} {i * ' *'}")
for i in range((a -1), 0, -1):
    findSpace = int((a - i) / 2)
    print(f"{findSpace * ' '} {i * ' *'}")