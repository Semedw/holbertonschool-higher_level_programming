#!/usr/bin/python3
if __name__ == '__main__':
    from calculator_1 import add, sub, mul, div
    import sys
    argv = sys.argv[1:]
    if len(argv) != 3:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)
    else:
        operators = [
            '+',
            '-',
            '*',
            '/'
        ]
        if argv[1] not in operators:
            print('Unknown operator. Available operators: +, -, * and /')
            exit(1)
        if argv[1] == '+':
            print(f'{argv[0]} + {argv[0]} =', add(int(argv[0]), int(argv[2])))
        if argv[1] == '-':
            print(f'{argv[0]} - {argv[0]} =', sub(int(argv[0]), int(argv[2])))
        if argv[1] == '*':
            print(f'{argv[0]} * {argv[0]} =', mul(int(argv[0]), int(argv[2])))
        if argv[1] == '/':
            print(f'{argv[0]} / {argv[0]} =', div(int(argv[0]), int(argv[2])))
