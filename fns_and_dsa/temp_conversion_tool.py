FAHRENHEIT_TO_CELSIUS_FACTOR =  5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 5/9
def convert_to_celsius(fahrenheit):
    return fahrenheit*FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return celsius*CELSIUS_TO_FAHRENHEIT_FACTOR

temperature = int (input("Enter the temperature to convert: "))
Unit = input ("Is this temperature in Celsius or Fahrenheit? (C/F): ") 
if Unit == "F": print(f"{temperature} ° {Unit} is {convert_to_celsius(temperature)} ° C")
elif Unit == "C" : print(f"{temperature} ° {Unit} is {convert_to_fahrenheit(temperature)} ° F")
else : print(f"Invalid temperature. Please enter a numeric value.")

