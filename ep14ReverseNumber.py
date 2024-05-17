def reverseNumber(number):
    num5string = number

    num5 = int(num5string)


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

def reverseNumberWithReturn(number):
    num5string = number

    num5 = int(num5string)


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
    result = str(d1) + str(d2) + str(d3) + str(d4) + str(d5)
    return result

isQuit = False
while not isQuit:
    num = input("Please Enter Number [if Quit type Q] :");
    if(num == "Q"):
        isQuit = True
        print("Good Bye !")
    else:
        if num.isdigit():
            # reverse_number(num)
            result = reverseNumberWithReturn(num)
            print(result)
        else:
            print("Invalid input")