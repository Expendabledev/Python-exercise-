your_postiveNum= int(input("Enter a positive integer Number: "))
for i in range(1, your_postiveNum+ 1):
    if i % 3 == 0 and i % 5 == 0:
        print("html ")
    elif i % 3 == 0:
        print("react")
    elif i % 5 == 0:
        print("bootstrap")
    else:
        print(i)
