str1 = 'Hello'
str2 = "bye"
str3 = """Good bye"""
print(str1)
print(str2)
print(str3)
print(str1+ ' '+str2)
print()
# Escape Sequence Characters
print("hjjkjhkj \n jdhkjas \t sdhsha") # \n -> next line \t -> Tab 
print(r"hjjkjhkj \n jdhkjas \t sdhsha")
print("She said \"Hi\"")
print("She said \\Hi\\")
print("She said \'Hi\'")

# Splicing 
strC = str1+str2+str3
print(strC)
print(strC[0:5]) # str[ starting_indx : ending_indx ]
print(strC[5:8])
print(strC[8:len(strC)])
print(strC[8:])
print(strC[0:5])
print(strC[-8:]) # negative index (Only for slicing)
print(strC[::2]) # step size of 2
print(strC[0:6:2]) # step size of 2 starting from index 0 to 6