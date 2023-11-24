#!/usr/bin/env python3

def admin_login(username, password):
    # your code here
      if username.upper() == "ADMIN" and password == "12345":
        return "Access granted"
    else:
        return "Access denied"
    

def hows_the_weather(temperature):
    # your code here
    if temperature < 40:
        return "It's brisk out there"
        elif temperature >= 40 and < 60:
        return "It's a little chilly out there!"
        elif temperature > 85:
            return "It's too dang hot out there"
            else:
                return "It's perfect out there!"

def fizzbuzz(num):
    # your code here
    if num == 3 or == 5:
        return "FizzBuzz"
        elif num == 3:
            return "Fizz"
            elif num == 5:
                return "Buzz"

def calculator(operation, num1, num2):
    # your code here
    if operation == "+":
        return num1 + num2
        elif operation == "-":
            return num1 - num2
            elif operation == "*":
                return num1 * num2
                elif operation == "/":
                    return num1 / num2
                    else:
                        print ("invalid input")
                        return None
