sample = [1,"abc","a",1]
cpsample = sample.copy()
sample.reverse()
if(cpsample == sample):
    print("Yes, list is palindrome")
else:
    print("No, list is not palindrome")