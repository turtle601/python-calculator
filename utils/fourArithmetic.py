def plus(array, operator):
    if operator == '+':
        return sum(array)

def minus(array, operator):
    if operator == '-':
        return array[1] - array[0]

def multiply(array, operator):
    if operator == '*':
        return array[1] * array[0]

def divide(array, operator):
    if operator == '/':
        return round(array[1] / array[0], 10)
