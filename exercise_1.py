number = 0
if number == 0: 
    previous_number = 0
else:
    previous_number = number - 1


for number in range(10):

    if number == 0: 
        previous_number = 0
    else:
        previous_number = number - 1

    print(f"Current Number {number} Previous Number {previous_number} Sum: {number + previous_number}")
    number += 1