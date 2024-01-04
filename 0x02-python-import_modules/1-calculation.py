#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1

a = 10
b = 5

result1 = calculator_1.add(a, b)
result2 = calculator_1.subtract(a, b)
result3 = calculator_1.multiply(a, b)
result4 = calculator_1.divide(a, b)

print(f"Addition of {a} and {b} is: {result1}")
print(f"Subtraction of {a} and {b} is: {result2}")
print(f"Multiplication of {a} and {b} is: {result3}")
print(f"Division of {a} and {b} is: {result4}")
