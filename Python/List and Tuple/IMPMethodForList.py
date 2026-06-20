list = [2,1,3]
print(list.append(4)) # most func return Null value or None
print(list)
print(list.sort()) # we can also sort strings in list (NOT STRINGS DATA TYPE)
print(list)
print(list.sort(reverse=True))
print(list)
print(list.reverse())
print(list)
print(list.insert(2,6))
print(list)
print(list.remove(2))
print(list)
print(list.pop(2)) # only pop have a return value of what has poped
print(list)
del(list[0]) # del is a keyword not a method of list
print(list)
print("Rock star".split()) # split is a method of string data type and it will return a list of words in the string
L = ["Rock star",10,11.56]
A = L
A[0] = "Python"
print(L) # both A and L are pointing to the same list in memory so changes in A will reflect in L and vice versa
# if we want to avoid this we can clone the list
B = L[:] # this will create a new list with the same elements as L
B[0] = "Java"
print(B)
print(L)