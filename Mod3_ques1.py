length = float(input("Enter the length of the zander in centimeters: "))
required_length = 42 - length
if length >= 42:
    print("The zander meets the required limit")
elif length < 42:
    print(f"The zander is {required_length} centimeters shorter than the required length. Please release the zander back to water.")
 
