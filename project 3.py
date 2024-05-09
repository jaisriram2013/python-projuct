password="sanjai"
loginpassword=input("Enter login password:")

while loginpassword!=password:
    print("Wrong password:")
    print("Try again:")
    loginpassword = input("Enter login password:")
print("You are logged in:")