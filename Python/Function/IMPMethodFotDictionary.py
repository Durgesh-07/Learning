student = {
    "name" : "rahul kumar",
    "subjects" : {
        "phy" : 97,
        "chem" : 69,
        "maths" : 98
    }
}

print("No. of key values pair is",len(student))
print(student)
print(student.keys()) # student.keys gives all keys
print(student.values()) # student.values gives all values
print(list(student.keys()))
print(list(student.values()))
print(student.items()) # this gives a tuple of student
print(list(student.items()))
pairs = list(student.items())
print(pairs[0])
# print(student["name2"]) This will give error as there is no key named "name2"
print(student.get("name2")) # student.get() does not gives ERROR which will be IMP later
new_dict = { # a new differnt dictionary
    "age" : 16,
    "city" : "ratlam"
}
student.update(new_dict) # add key value pairs to student from new_dist
print(student)
student.update({"name" : "neha kumar"}) # as "name" key is already in student it will override the existing
print(student)