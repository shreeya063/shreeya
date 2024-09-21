INCH_TO_CM = 2.54
while True:
    inches = float(input("Enter a value in inches (enter a negative value to quit): "))
    if inches < 0:
        print("Negative value entered. Program ending.")
        break
    centimeters = inches * INCH_TO_CM
    print(f"{inches} inches is equal to {centimeters}centimeters.")
