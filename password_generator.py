import secrets
import string
import argparse

def generate_password(length=16, use_upper=True, use_digits=True, use_symbols=True):
    alphabet = string.ascii_lowercase
    if use_upper:
        alphabet += string.ascii_uppercase
    if use_digits:
        alphabet += string.digits
    if use_symbols:
        alphabet += "!@#$%^&*()-_=+[]{};:,.<>/?"
    while True:
        pwd = ''.join(secrets.choice(alphabet) for _ in range(length))
        if (not use_upper or any(c.isupper() for c in pwd)) and \
           (not use_digits or any(c.isdigit() for c in pwd)) and \
           (not use_symbols or any(c in '!@#$%^&*()-_=+[]{};:,.<>/?' for c in pwd)):
            return pwd

def main():
    parser = argparse.ArgumentParser(description='Secure Password Generator')
    parser.add_argument('-l','--length', type=int, default=16, help='Password length')
    parser.add_argument('--no-upper', action='store_true', help='Disable uppercase letters')
    parser.add_argument('--no-digits', action='store_true', help='Disable digits')
    parser.add_argument('--no-symbols', action='store_true', help='Disable symbols')
    args = parser.parse_args()
    pwd = generate_password(length=args.length, use_upper=not args.no_upper,
                            use_digits=not args.no_digits, use_symbols=not args.no_symbols)
    print(pwd)

if __name__ == '__main__':
    main()
