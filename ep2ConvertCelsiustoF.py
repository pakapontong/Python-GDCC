def celsius_to_fahrenheit(celsius):

    fahrenheit = (celsius * 9)/5 + 32
    return fahrenheit

def main():
    celsius = float(input("Enter Your Celsius: "))
    fahrenheit = celsius_to_fahrenheit(celsius)
    print("Fahrenheit:", fahrenheit)

if __name__ == "__main__":
    main()


# -------------------------------------------------------------------

celsius = float(input("Enter your Celsius : "))
fahrenheit = (celsius * 9)/5 + 32
print("%.2f Celsius is equal to %.2f Fahrenheit" % (celsius, fahrenheit));