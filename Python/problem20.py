'''Problem 20: Factorial digit sum

    William Ikenna-Nwosu (wiknwo)

    n! means n × (n − 1) × ... × 3 × 2 × 1

    For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
    and the sum of the digits in the number 10! is 
    3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

    Find the sum of the digits in the number 100!
'''
import math
def main():
    digits = str(math.factorial(100))
    running_sum = 0
    for digit in digits:
        running_sum += int(digit)
    print(running_sum)
if __name__ == '__main__':
    main()