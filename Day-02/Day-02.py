print("Assign multiple values to multiple variables")
num1, num2, num3 = 10, 20, 30
print("number1 values num1")
print("number1 value", num1)
print("number2 value", num2)
print("number3 value", num3)
print("All variable refferences are:", id(num1), id(num2), id(num3))
print("Assign single value to multiple version")
num1, num2, num3 =257,257,257
print("number1 value num1")
print("number1 value", num1)
print("number2 value", num2)
print("number3 value", num3)
print("All variable refferences are:", id(num1), id(num2), id(num3))
print("Swapping two numbers")
a, b = 10, 20
print("Before swapping")
print(a, b, id(a), id(b))
a, b = b, a
print(a, b,id(a), id(b))
