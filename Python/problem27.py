'''Problem 27: Quadratic Primes

    William Ikenna-Nwosu (wiknwo)
'''
from eulerlib import primes
import time

# Time at start of execution
start = time.time()

def is_prime(number):
    '''Function to determine if number is prime

        Args:
            number(int): number

        Raises: 

        Returns:
            boolean(bool): boolean
    '''
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

def main():
    primes_below_thousand = primes(1000)
    primes_below_thousand_copy = primes_below_thousand[:]
    n = 0
    product_of_coefficients = -1

    # Looping through quadratic equation
    for b in primes_below_thousand:
        for a in primes_below_thousand:
            i = 0
            # Positive a and b
            while True: 
                quadratic_expression = i**2 + (a * i) + b
                if quadratic_expression not in primes_below_thousand_copy:
                    if is_prime(quadratic_expression):
                        primes_below_thousand_copy.append(quadratic_expression)
                    else:
                        if i - 1 > n:
                            n = i - 1
                            product_of_coefficients = a * b
                        break
                i += 1
            i = 0
            # Negative a and positive b
            while True:
                quadratic_expression = i**2 - (a * i) + b
                if quadratic_expression not in primes_below_thousand_copy:
                    if is_prime(quadratic_expression) and quadratic_expression > 0:
                        primes_below_thousand_copy.append(quadratic_expression)
                    else:
                        if i - 1 > n:
                            n = i - 1
                            product_of_coefficients = -1 * a * b
                        break
                i += 1
    print(product_of_coefficients)
    print(primes_below_thousand_copy)
    print(time.time() - start) # Printing total time of execution in milliseconds
    

if __name__ == '__main__':
    main()