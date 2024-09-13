def create_operation_function(operation):
    def operation_function(x, y):
        if operation == 'add':
            return x + y
        elif operation == 'subtract':
            return x - y
        elif operation == 'multiply':
            return x * y
        elif operation == 'divide':
            return x / y
        else:
            raise ValueError("Unsupported operation")
    return operation_function

if __name__ == "__main__":
    # 动态生成不同的操作函数
    add = create_operation_function('add')
    subtract = create_operation_function('subtract')
    multiply = create_operation_function('multiply')
    divide = create_operation_function('divide')
    
    # 使用这些生成的函数
    print("Addition: 5 + 3 =", add(5, 3))
    print("Subtraction: 5 - 3 =", subtract(5, 3))
    print("Multiplication: 5 * 3 =", multiply(5, 3))
    print("Division: 6 / 3 =", divide(6, 3))
