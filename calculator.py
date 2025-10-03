def addition(a, b):
    """
    Returns the sum of a and b.
    Args:
        a (int or float): First number.
        b (int or float): Second number.
    Returns:
        int or float: The sum of a and b.
    """
    sum_of = a + b
    return sum_of
print(addition(7.5, 5))


def subtraction(a, b):
    """
    Returns the difference of a and b.
    Args:
        a (int or float): First number.
        b (int or float): Second number.
    Returns:
        int or float: The result of a - b.
    """
    difference = a - b
    return difference
print(subtraction(4, 65))

def multiplication(a, b):
    """
    Returns the product of a and b.
    Args:
        a (int or float): First number.
        b (int or float): Second number.
    Returns:
        int or float: The product of a and b.
    """
    times = a * b
    return times
print(multiplication(16, 7))

def division(a, b):
    """
    Returns the quotient of a divided by b.
    Args:
        a (int or float): Numerator.
        b (int or float): Denominator.
    Returns:
        float: The result of a / b.
    """
    divide = a / b
    return divide
print(division(78, 45))

def modulus(a, b):
    """
    Returns the remainder of a divided by b.
    Args:
        a (int or float): Numerator.
        b (int or float): Denominator.
    Returns:
        int or float: The remainder after division.
    """
    rem = divmod(a, b)
    return rem[1]
print(modulus(15, 10))

def exponentiation(a, b):
    """
    Returns a raised to the power of b.
    Args:
        a (int or float): Base number.
        b (int or float): Exponent.
    Returns:
        int or float: The result of a ** b.
    """
    expo = a ** b
    return expo
print(exponentiation(5, 2))  

def floor_division(a, b):
    """
    Returns the floor division of a by b.
    Args:
        a (int or float): Numerator.
        b (int or float): Denominator.
    Returns:
        int: The result of a // b.
    """
    floor = divmod(a, b)
    return floor[0]
print(floor_division(25, 5))

def calculator(num1, operation, num2):
    """
    Performs a calculation based on the given operation and numbers.
    Args:
        num1 (int or float): The first number.
        operation (str): The operation to perform. Supported values: '+', '-', '*', '/', '%', '**', '//'.
        num2 (int or float): The second number.
    Returns:
        int or float: The result of the calculation, or an error message if the operation is invalid.
    Example:
        result = calculator(5, '+', 3)  # Returns 8
    """
    if operation == "+":
        answer =  num1 + num2
    elif operation == "-":
        answer = num1 - num2
    elif operation == "*":
        answer = num1 * num2
    elif operation == "/":
        answer = num1 / num2
    elif operation == "%":
        x = divmod(num1, num2)
        answer = x[1]
    elif operation == "**":
        answer = num1 ** num2
    elif operation == "//":
        x = divmod(num1, num2)
        answer = x[0] 
    else:
        print("Calculation invalid. Try again!")
    return answer
print(calculator(5, "**", 4))