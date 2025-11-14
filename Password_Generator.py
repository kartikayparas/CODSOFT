import secrets
import string
import argparse

def generate(length=12, use_symbols=True, use_upper=True, use_digits=True):
    alphabet = string.ascii_lowercase
    if use_upper: alphabet += string.ascii_uppercase
    if use_digits: alphabet += string.digits
    if use_symbols: alphabet += "!@#$%^&*()-_=+[]{};:,.<>/?"
    if length < 4:
        raise ValueError("Length should be at least 4")
    return ''.join(secrets.choice(alphabet) for _ in range(length))

def main():
    p = argparse.ArgumentParser(description="Password Generator")
    p.add_argument("--length", type=int, default=12)
    p.add_argument("--no-symbols", action="store_true")
    p.add_argument("--no-upper", action="store_true")
    p.add_argument("--no-digits", action="store_true")
    args = p.parse_args()
    pwd = generate(args.length, not args.no_symbols, not args.no_upper, not args.no_digits)
    print("Password:", pwd)

if __name__ == "__main__":
    main()
