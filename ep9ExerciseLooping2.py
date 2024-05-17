AllList = [50, 5, 15, -8]
print(AllList[0])

#Inititalization
index = 0;
maxlength = len(AllList)
sum = 0
total = 0;

#condition
while index < len(AllList):
    total += AllList[index] # total = AllList 
    index += 1

print("sum : ", total)


# กำหนดตัวแปรเพื่อเก็บผลรวม
total = 0

# ใช้ลูปเพื่อหาผลรวมของรายการ
for num in AllList:
    total += num

# พิมพ์ผลรวม
print("ผลรวมของรายการ:", total)
