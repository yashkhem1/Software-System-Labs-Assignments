#!python3

import argparse


# ap = argparse.ArgumentParser()
# ap.add_argument("--first_name", required=True, help="first name")
# ap.add_argument("--last_name", required=True, help="last name")
# ap.add_argument("--roll_no", type=int, required=True, help="roll number")
# ap.add_argument("--dept", required=True, help="department")
# args = vars(ap.parse_args()

def isPrime(n):
    for i in range(2, n):
        if n % i == 0:
            return False

    return True


def numPrimes(n1, n2):
    c = 0
    for i in range(n1, n2 + 1):
        if isPrime(i):
            c = c + 1
    return c


result = ''
error = 0
ap = argparse.ArgumentParser()
ap.add_argument("--check_prime", type=int)
ap.add_argument("--range", nargs='+', type=int)
args = vars(ap.parse_args())
# print(len(args))

try:

    if args["check_prime"] is None and args["range"] is None:
        raise ValueError('Error : At least one of the following arguments are required: --check_prime, --range')
        error = 1
    else:
        if args["check_prime"] is not None:
            if args["check_prime"] not in range(1, 1001):
                raise ValueError('Error : Please enter a value between 1 and 1000 only')
                error = 1
            elif isPrime(args["check_prime"]):
                result = result + 'Yes '
            else:
                result = result + 'No '

        if args["range"] is not None:
            if args["range"][1] not in range(1, 1001) or args["range"][0] not in range(1, 1001):
                raise ValueError('Error : Please enter a value between 1 and 1000 only')
                error = 1
            else:
                result = result + str(numPrimes(args["range"][0], args["range"][1]))

        if error == 0:
            print(result)

except ValueError as e:
    print(e)
