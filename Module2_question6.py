import random
three_digit_code = str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9))
four_digit_code = str(random.randint(1, 6)) + str(random.randint(1, 6)) + str(random.randint(1, 6)) + str(random.randint(1, 6))
print("The 3-digit combination lock code is: ", three_digit_code)
print("The 4-digit combination lock code is: ", four_digit_code)
