class Box: 

    # Class Attribute
    # width = 0;
    # height = 0;
    # deep = 0;
    # maxweight = 0;

     
    def __init__(self,w,h=None,d=None,maxw=None): # self เป็น รีเซิปเวิส
        # if maxw == 0:
        #     self.width = w
        #     self.height = h
        #     self.deep = d
        # else:
        #     self.width = w
        #     self.height = h
        #     self.deep = d
        #     self.maxweight = maxw
        if h is None and d is None:
            self.width = w
            self.height = w
            self.deep = w
            self.maxweight = maxw
            self.__Capacity = w * w * w
        else:
            self.width = w
            self.height = h
            self.deep = d
            self.maxweight = maxw
            self.__Capacity = w * h * d


    # def __init__(self,w,maxw): #python ไม่สามารถเขียน constructor overloading ได้
    #     self.width = w
    #     self.height = w
    #     self.deep = w
    #     self.maxweight = maxw


    def Rental(self,w,h,d,maxw): # ต้องใช้ self เสมอ rental
        print("Capacity : {}".format(self.__Capacity))
        Fees = 0
        if self.maxweight > maxw:
            Fees = w * h * d * maxw
        return Fees 

    def getCapacity(self):
        return self.__capacity

#Box Instant 
myBox = Box(15,15,25,23)
# capacity = myBox.__Capacity
capacity = myBox.getCapacity()
#Named Parameter
cubicBox = Box(w=15,maxw=500)
print("My Box Dimension {} {} {} ".format(myBox.width, myBox.height, myBox.deep))
print("Cubic Dimension {} {} {} ".format(cubicBox.width, cubicBox.height, cubicBox.deep))
