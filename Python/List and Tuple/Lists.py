student = ["Durgesh",19,"KIIT"] # this is List not array (same as array)
print(student)
print(type(student))
str = "Durgesh"
print(str[0])
# str[0] = "B" <- this command will not work as strings are immutable
student[0] = "Jatin" # lists are mutable
print(student)
print(student[0:2])