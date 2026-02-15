try:
    num1=int(input("Enter numerator"))
    num2=int(input("Enter denominator"))
    res=num1/num2
    print("Result:",res)
except ZeroDivisionError:
    print("Error:Cannot divide by zero!")
except ValueError:
    print("Error:Please enter valid integers")
