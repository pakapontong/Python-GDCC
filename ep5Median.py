def find_median(data):
    
    sorted_data = sorted(data)
    n = len(sorted_data)
    if n % 2 == 0:
        mid_right = n // 2 
        mid_left = mid_right - 1
        median = (sorted_data[mid_left] + sorted_data[mid_right]) / 2
    else:
        mid = n // 2 
        median = sorted_data[mid]
    return median

def main():
    data = input("Enter Your Number: ") #รับข้อมูลจากผู้ใช้
    data_list = [float(x) for x in data.split(',')] #แปลงข้อมูลที่รับเข้ามาเป็นรายการข้อมูล
    median = find_median(data_list) #เรียกใช้ฟังก์ชันหาค่ากลาง
    print("Median : ", median) #แสดงผลลัพธ์

if __name__ == "__main__":
    main()

# ------------------------------------------------------------------
a = float(input("Input first number : "))
b = float(input("Input second number : "))
c = float(input("Input third number : "))

if a > b:
    if a < c:
        median = a
    elif b > c:
        median = b
    else:
        median = c
else:
    if a > c:
        median = a
    elif b > c:
        median = b
    else: 
        median = c

print("The median is", median);