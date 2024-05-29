def admin_login(username, password):
    if username.lower() == "admin" and password == "12345":
        return "Access granted"
    else:
        return "Access denied"
def hows_the_weather(temperature):
    if temperature < 32:  # Adjusted to match test expectations
        return "It's too cold!"
    elif 32 <= temperature < 40:  # Adjusted for "brisk"
        return "It's brisk out there!"
    elif 40 <= temperature < 64:  # Adjusted for "chilly"
        return "It's a little chilly out there!"
    elif 64 <= temperature < 84:  # Adjusted for "perfect"
        return "It's perfect out there!"
    else:  # Adjusted to match test expectations
        return "It's too dang hot out there!"






def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num  
def calculator(operation, num1, num2):
    valid_operations = ["+", "-", "*", "/"]
    if operation not in valid_operations:
        print("Invalid operation!")
        return None
    
    try:
        if operation == "+":
            return num1 + num2
        elif operation == "-":
            return num1 - num2
        elif operation == "*":
            return num1 * num2
        elif operation == "/":
            if num2!= 0:
                return num1 / num2
            else:
                raise ValueError("Cannot divide by zero.")
    except Exception as e:
        print(str(e))
        return None



