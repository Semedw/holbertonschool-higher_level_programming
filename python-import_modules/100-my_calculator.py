#!/usr/bin/python3
if __name__ == '__main__':
    from calculator_1.py import (add, sub, mul, div)
    import sys
    argv = sys.argv[1:]
    if len(argv) != 3:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        print(1)

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
        print(add(int[argv[0]], int(argv[2])))
    if argv[1] == '-':
        print(sub(int[argv[0]], int(argv[2])))
    if argv[1] == '*':
        print(mul(int[argv[0]], int(argv[2])))
    if argv[1] == '/':
        print(div(int[argv[0]], int(argv[2])))
