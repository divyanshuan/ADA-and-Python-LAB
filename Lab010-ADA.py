import random


def is_prime(num: int, k=20) -> bool:
    '''
    Primality Testing using Fermat's Principle
    Inputs: num: a value to test for primality, n>3; k: a parameter that determines the number of times to test for primality
    Output: False if n is composite, otherwise True
    '''
    # when num <= 3 cal in O(1)
    if num <= 1:
        return False
    if num == 2 or num == 3:
        return True
    # pick a random a between [2,n-2] for k times and check for fermat's primality
    for i in range(k):
        a = random.randint(2, num-2)
        res = (a**(num-1)) % num
        if res != 1:
            return False

    return True


if __name__ == "__main__":
    num = int(input("Enter a number: "))
    print("\nAccording to Fermat's primality test:")
    if is_prime(num):
        print(f"{num} is a prime number")
    else:
        print(f"{num} is a composite number")