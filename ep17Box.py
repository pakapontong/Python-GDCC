class Box: #ใช้กับงานคำนวณ KPI, โบนัส 

    # Class Attribute
    width = 0;
    height = 0;
    deep = 0;
    maxweight = 0;

    def Rental(self,w,h,d,maxw): # ต้องใช้ self เสมอ rental
        Fees = 0
        if self.maxweight > maxw:
            Fees = w * h * d * maxw
        return Fees 

myBox = Box() #constructor ตัวสร้าง object ก่อสร้างได้มาจะได้สิ่งที่อยู่ซ้ายมือคือ object object อยู่บน memory
myBox.width = 10;
myBox.height = 10;
myBox.deep = 10;
myBox.maxweight = 2000

yourBox = Box()
print("My Box Dimension {} {} {} ".format(myBox.width, myBox.height, myBox.deep))
print("Your Box Dimension {} {} {} ".format(yourBox.width, yourBox.height, yourBox.deep))

yourBox = myBox #รับค่าจาก myBox
print("Your Box Dimension {} {} {} ".format(yourBox.width, yourBox.height, yourBox.deep))
result = myBox.Rental(10,5,5,500)
print("Fees {}".format(result))


list1 = [1,2,3,4,5]
list2 = list1
print(list1)
print(list2)
list1.remove(1)
print(list1)
print(list2)


name = "Hello"
name1 = name 
print(name)
print(name1)
print(name[0])
name = "Gello"
print(name)
print(name1)