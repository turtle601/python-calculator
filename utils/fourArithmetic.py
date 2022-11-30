def plus(array, operator):
    if operator == '+':
        return sum(array)

def minus(array, operator):
    if operator == '-':
        return array[0] - array[1]

def multiply(array, operator):
    if operator == '*':
        return array[0] * array[1]

def divide(array, operator):
    if operator == '/':
        return round(array[0] / array[1], 10)

def getRest(array, operator):
    if operator == '%':
        return array[0] % array[1]