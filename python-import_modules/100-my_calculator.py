#!/usr/bin/python3
if __name__ == '__main__':
    from calculator_1 import add, sub, mul, div
    import sys
    argv = sys.argv[1:]
    if len(argv) != 3:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
    else:
        operators = [
            '+',
            '-',
            '*',
            '/'
        ]
        if argv[1] not in operators:
            print('Unknown operator. Available operators: +, -, * and /')
            print(1)
        
        if argv[1] == '+':
            print('{} + {} ='.format(argv[0], argv[2]), add(int(argv[0]), int(argv[2])))
        if argv[1] == '-':
            print('{} - {} ='.format(argv[0], argv[2]), sub(int(argv[0]), int(argv[2])))
        if argv[1] == '*':
            print('{} * {} ='.format(argv[0], argv[2]), mul(int(argv[0]), int(argv[2])))
        if argv[1] == '/':
            print('{} / {} ='.format(argv[0], argv[2]), div(int(argv[0]), int(argv[2])))
