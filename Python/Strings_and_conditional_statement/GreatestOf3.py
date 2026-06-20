num1 = input("Enter num1: ")
num1 = int(num1)
num2 = input("Enter num2: ")
num2 = int(num2)
num3 = input("Enter num3: ")
num3 = int(num3)
if(num1>num2):
    if(num1>num3):
        print("num1 is greatest")
    else:
        print("num3 is greatest")
else:
    if(num2>num3):
        print("num2 is greatest")
    else:
        print("num3 is greatest")