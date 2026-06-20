tup = (1,2,3) 
print(tup)
print(tup[1])
# tup[0] = 4 <- tuple is also immutable like strings
print(type(tup))
tup1 = (1) # this is not a tuple its a integer
print(type(tup1))
tup2 = (1,) # tuple for single element
print(type(tup2))
print(tup[:2])