def ConversionSeconds2Days(seconds):
    Days = seconds // (86400)
    seconds = seconds % (86400)
    Hours = seconds // (3600)
    seconds = seconds % (3600)
    Minutes = seconds // (60)
    seconds = seconds % (60)

    result = str(Days) + ":" + str(Hours) + ":" + str(Minutes) + ":" + str(seconds)

    return result

# Calling Function
seconds = int(input("Input time in seconds : "));
result = ConversionSeconds2Days(seconds)
print(result)