def multiply_by_2(x):
    return x * 2

def sum_2(x):
    return x + 2

def divide_by_2(x):
    return x / 2   

def operacion(func, x):
    result = []
    
    for i in x:
        result.append(func(i))
    
    return result

num = [1, 2, 3, 4, 5]
print(operacion(multiply_by_2, num))
print(operacion(sum_2, num))
print(operacion(divide_by_2, num))