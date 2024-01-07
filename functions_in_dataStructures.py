def apply_operations(x):
    operations = [abs, float]
    result = []
    
    for operation in operations:
        result.append(operation(x))
        
    return result

print(apply_operations(-2))