#import formulas
from formulas import *
import sys

def main():
    total = sys.argv
    operation = sys.argv[1]
    values = sys.argv[2:]
    if len(total) <= 1:
        sys.exit('Need to provide operator')
    elif len(total) <= 3:
        sys.exit('Need to provide at least two values.')
    else:
        if operation == "add":
            addition = add(values)
            print(addition)
        elif operation == "subtract":
            sub = subtract(values)
            print(sub)
        elif operation == "multiply":
            mult = multiply(values)
            print(mult)
        elif operation == "divide":
            div = divide(values)
            print(div)
        elif operation != "add" and operation != "subtract" and operation != "multiply" and operation != "divide":
            print("Valid operator names (add, subtract, multiply, divide)")

if __name__ == '__main__':
    main()
    