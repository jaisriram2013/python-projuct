numbers=[5,151,145,18,419,168,16,84,48]
even=[]
odd=[]
for i in numbers:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print("Even List-",even)
print("Odd List",odd)