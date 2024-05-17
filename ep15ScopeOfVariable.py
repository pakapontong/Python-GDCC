total = 0;

def addMe(a,b):
    global total
    total = a+b;
    print("inside Function : {}".format(total));

def subtractMe(a,b):
    total = a
    if a > b:
        total = a - b;
        c = 10;
        print("Inside A block {}".format(total))
    else:
        total = b - a;
        print("Inside B block {}".format(total))
    print("inside Function : {}".format(total));
    print("inside Function with {}".format(c));


subtractMe(10,5);
print("Outside Function : {}".format(total));