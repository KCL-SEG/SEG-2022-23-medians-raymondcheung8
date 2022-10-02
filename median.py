"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break

numbers.sort()

if len(numbers) % 2 == 1:
    print(numbers[len(numbers) // 2])
else:
    x = numbers[len(numbers) // 2] - 1
    y = x + 1

    print((x + y) / 2)

#print(numbers)