print("if you convert Fahrenhit to Celsius so press 'F', If you convert Celsius to Fahrenhit so press 'C'")
inp =input("Enter Here: ")
if inp == 'F':
    f = float(input("Enter temperature in Fahrenheit: "))
    c = (f - 32) * 5 / 9
    print("Celsius:", c,"°C")
elif inp == 'C':
    c = float(input("Enter temperature in Celsius: "))
    f = (c * 9 / 5) + 32
    print("Fahrenheit:", f,"°F")
else:
    print("Only Press F or C")