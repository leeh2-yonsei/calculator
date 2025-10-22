import time

print('-' * 20)
print('\033[1mCalculator Opened!\033[0m')
print('-' * 20)

while True:
    time.sleep(1)
    sentence = input("Enter an expression: ").replace(' ', '')

    # Break
    if sentence == 'exit':
        print('\033[1;31mGoodbye!\033[0m')
        break

    # Check if the formula is appropriate
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

    # Get Sentence Again if wrong
    if wrong or (operator is None):
        print("\033[31mThe Formula is wrong!\033[0m")
        continue

    result = 0
    if operator == '+':
        num1, num2 = sentence.split('+')
        result = float(num1) + float(num2)
    elif operator == '-':
        num1, num2 = sentence.split('-')
        result = float(num1) - float(num2)
    elif operator == '/':
        num1, num2 = sentence.split('/')
        # continue if num2 == 0
        if float(num2) == 0.:
            print("\033[31mYou cannot divide by zero!\033[0m")
            continue

        result = float(num1) / float(num2)
    elif operator == 'x':
        num1, num2 = sentence.split('x')
        result = float(num1) * float(num2)

    print(f'\033[32m{sentence} = {result: .3f}\033[0m')





