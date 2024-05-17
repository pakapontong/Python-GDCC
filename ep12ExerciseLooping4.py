def count_characters(text):

    char_count = 0
    digit_count = 0

    
    for char in text:
        
        if char.isalpha():
            char_count += 1
        elif char.isdigit():
            digit_count += 1

    
    print("จำนวนตัวอักษร:", char_count)
    print("จำนวนตัวเลข:", digit_count)


user_input = input("Please Your Message : ")

count_characters(user_input)


#-----------------------------------------------

inputString = "10th Anniversary"
digit = alpha = 0;
for char in inputString:
    isAlpha = char.isalpha()
    isDigit = char.isdigit()
    if isAlpha:
        char += 1;
    if  isDigit:
        char += 1;