# Explanation of Code

### 1. Breack Exception
```python
if sentence == 'exit':
    print('\033[1;31mGoodbye!\033[0m')
    break
```
If exit is detected, exit the program

### 2. A Feasibility Test
```python
wrong = False
operator = None  # To verify that there is only one operator
for char in sentence:
    if not (char in '0123456789+-x/.'):
        wrong = True
        break
    if char in ['+', '-', 'x', '/']:
        if operator is not None:
            wrong = True
        operator = char
```
* Verify that the given statement consists of only numbers and operators.
* Verify that there is only one operator

### 3. Calcuation
```python
result = 0
if operator == '+':
    num1, num2 = sentence.split('+')
    result = float(num1) + float(num2)
elif operator == '-':
    num1, num2 = sentence.split('-')
    result = float(num1) - float(num2)
elif operator == '/':
    num1, num2 = sentence.split('/')
    result = float(num1) / float(num2)
elif operator == 'x':
    num1, num2 = sentence.split('x')
    result = float(num1) * float(num2)
```
The operation is performed according to the given operator.


# Input and Output
1. Input: a sentence consisting of a numbers and an operator
2. Output: Result of Calculation