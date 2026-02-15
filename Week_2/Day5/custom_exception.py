class NegativeNumberError(Exception):
    pass

try:
    number = int(input("Enter a positive number: "))
    
    if number < 0:
        raise NegativeNumberError("Negative numbers are not allowed!")
    
    print("You entered:", number)

except NegativeNumberError as e:
    print("Custom Error:", e)

except ValueError:
    print("Error: Please enter a valid integer.")