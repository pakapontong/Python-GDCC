# Get 5 Digit Input from Keyboard
num5string = input("Please Enter 5 Digit Numbers ") 

# Convert String to Number
num5 = int(num5string)

# Extract Number
d1 = num5 % 10 #5
num5 = num5 // 10 #1234

d2 = num5 % 10 #4
num5 = num5 // 10 #123

d3 = num5 % 10 #3
num5 = num5 // 10 #12

d4 = num5 % 10 #2
num5 = num5 // 10 #1

d5 = num5 % 10 #1
num5 = num5 // 10 #0

print("{}{}{}{}{}".format(d1,d2,d3,d4,d5))