def calculate_total(a, b):  # Parameters: a and b
    total = a + b           # Task: Addition
    return total            # Output: Sum of a and b

result = calculate_total(5, 7)  # Calling the function with inputs 5 and 7
print(result)  # Output: 12
string_length = len("Hello, World!")  # Output: 13
list_length = len([1, 2, 3, 4, 5])   # Output: 5
total = sum([10, 20, 30, 40, 50])  # Output: 150
highest = max([5, 12, 8, 23, 16])  # Output: 23
lowest = min([5, 12, 8, 23, 16])  # Output: 5
def function_name():
    pass
'''Placeholder: "pass" acts as a temporary placeholder for future code that you intend to write within a function or a code block.
Syntax Requirement: In many programming languages like Python, using "pass" is necessary when you define a function or a conditional block. It ensures that the code remains syntactically correct, even if it doesn't do anything yet.
No Operation: "pass" itself doesn't perform any meaningful action. When the interpreter encounters "pass", it simply moves on to the next statement without executing any code'''
def multiply(a, b):
    """
    This function multiplies two numbers.
    Input: a (number), b (number)
    Output: Product of a and b
    """
    print(a * b)
multiply(2,6)
global_variable = "I'm global"
def example_function():
    local_variable = "I'm local"
    print(global_variable)  # Accessing global variable
    print(local_variable)   # Accessing local variable
example_function()
print(global_variable)  # Accessible outside the function
# print(local_variable)  # Error, local variable not visible here
def custom():
    global var
    var = 12 # Declaring a global variable inside the function
    print(var)      # Output: 12
custom()
def addItems(list):
    list.append("Three")
    list.append("Four")

myList = ["One","Two"]

addItems(myList)

print(myList)
def printAll(*args): # All the arguments are 'packed' into args which can be treated like a tuple
    print("No of arguments:", len(args)) 
    for argument in args:
        print(argument)
#printAll with 3 arguments
printAll('Horsefeather','Adonis','Bone')
#printAll with 4 arguments
printAll('Sidecar','Long Island','Mudslide','Carriage')
def printDictionary(**args):
    for key in args:
        print(key + " : " + args[key])

printDictionary(Country='Canada',Province='Ontario',City='Toronto')
