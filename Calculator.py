import argparse
import operator
ops = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
    "^": operator.pow
}

def calc(a, b, op):
    if op not in ops:
        raise ValueError("Unsupported operator.")
    if op == "/" and b == 0:
        return "Undefined"
    return ops[op](a, b)

def main():
    p = argparse.ArgumentParser(description="Calculator")
    p.add_argument("a", type=float, nargs='?', help="First number")
    p.add_argument("op", type=str, nargs='?', help="operator (+ - * / ^)")
    p.add_argument("b", type=float, nargs='?', help="Second number")
    args = p.parse_args()
    if args.a is None or args.op is None or args.b is None:
        # interactive
        a = float(input("First number: "))
        op = input("Operator (+ - * / ^): ").strip()
        b = float(input("Second number: "))
    else:
        a, op, b = args.a, args.op, args.b
    try:
        result = calc(a, b, op)
    except Exception as e:
        print("Error:", e)
    else:
        print("Result:", result)

if __name__ == "__main__":
    main()
