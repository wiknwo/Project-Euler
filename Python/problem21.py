'''Problem 21: Amicable Numbers

    William Ikenna-Nwosu (wiknwo)

    Let d(n) be defined as the sum of proper divisors of 
    n (numbers less than n which divide evenly into n).
    If d(a) = b and d(b) = a, where a ≠ b, then a and b 
    are an amicable pair and each of a and b are called 
    amicable numbers.

    For example, the proper divisors of 220 are 1, 2, 4, 5, 
    10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. 
    The proper divisors of 284 are 1, 2, 4, 71 and 142; so 
    d(284) = 220.

    Evaluate the sum of all the amicable numbers under 10000.
'''
def sum_proper_divisors(number):
    divisors = []
    for i in range(1, number):
        if number % i == 0:
            divisors.append(i)
    return sum(divisors)

def is_amicable_number(number):
    b = sum_proper_divisors(number)
    c = sum_proper_divisors(b)

    if c == number and b != number:
        # Amicable pair found: sum(proper_divisors(d_n)) == number
        print("d(number) = b, d(b) = number, d({0}) = {1}, d({1}) = {0}".format(number, b))
        return True
    return False

def main():
    amicable_numbers = []
    for i in range(1, 10000):
        if i in amicable_numbers:
            continue
        # If i is an amicable number, append i and its pair
        if is_amicable_number(i):
            amicable_numbers.append(i)
            amicable_numbers.append(sum_proper_divisors(i))
        
    print(sum(amicable_numbers))
if __name__ == '__main__':
    main()