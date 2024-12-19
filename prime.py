a = int(input("Enter a input to find prime numbers"))
for i in range(a):
    findPrimeNo = True
    if(i == 0 or i == 1):
        print(i, "is prime number")
    else:        
        for k in range(2, i):
           if(i % k == 0):               
               findPrimeNo = False
               break
        if(findPrimeNo):
            print(i, "is prime number")

# for i in range(1, a):
#     if(i % 2 == 0):
#         print("number is ", i)
#         # break
#     else:
#         print("number is ", i)

