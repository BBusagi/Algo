def fibonacci(number):
    if number == 0: return 0
    elif number == 1 : return 1
    else:
        return fibonacci(number - 1) + fibonacci(number - 2)

input_number = 10
result = fibonacci(input_number)
print(result)