def convert_seconds_to_days(seconds):
    # หาจำนวนวินาทีในหนึ่งวัน
    seconds_per_day = 24 * 60 * 60
    
    # แปลงวินาทีเป็นวัน
    days = seconds // seconds_per_day
    
    # หาจำนวนวินาทีที่เหลือท้ายที่ไม่ถึงหนึ่งวัน
    remaining_seconds = seconds % seconds_per_day
    
    # แยกวินาทีเป็นชั่วโมง นาที และวินาที
    hours = remaining_seconds // 3600
    remaining_seconds %= 3600
    minutes = remaining_seconds // 60
    seconds = remaining_seconds % 60
    
    return days, hours, minutes, seconds

# รับข้อมูลจากผู้ใช้ผ่านทางคีย์บอร์ด
seconds = int(input("Input time in seconds : "))

# แปลงวินาทีเป็นวัน ชั่วโมง นาที วินาที
days, hours, minutes, seconds = convert_seconds_to_days(seconds)

# แสดงผลลัพธ์
print(f"{days} D {hours} H {minutes} M {seconds} S")