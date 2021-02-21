'''Problem 23: Non-Abundant Sums

    William Ikenna-Nwosu (wiknwo)

    A perfect number is a number for which the sum of 
    its proper divisors is exactly equal to the number. 
    For example, the sum of the proper divisors of 28 
    would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 
    is a perfect number.

    A number n is called deficient if the sum of its 
    proper divisors is less than n and it is called 
    abundant if this sum exceeds n.

    As 12 is the smallest abundant number, 1 + 2 + 3 + 4 
    + 6 = 16, the smallest number that can be written as 
    the sum of two abundant numbers is 24. By mathematical 
    analysis, it can be shown that all integers greater 
    than 28123 can be written as the sum of two abundant 
    numbers. However, this upper limit cannot be reduced 
    any further by analysis even though it is known that 
    the greatest number that cannot be expressed as the 
    sum of two abundant numbers is less than this limit.

    Find the sum of all the positive integers which 
    cannot be written as the sum of two abundant numbers.
'''
def sum_proper_divisors(number):
    divisors = []
    for i in range(1, number):
        if number % i == 0:
            divisors.append(i)
    return sum(divisors)

def is_abundant(number):
    return sum_proper_divisors(number) > number

def findPairs(alist, number):
    for i in range(len(alist)):
        if (number - alist[i]) in alist:
            return True
    return False

def main():
    abundant_numbers = []
    non_abundant_sum = 0

    for i in range(28124):
        if is_abundant(i):
            abundant_numbers.append(i)
    
    for i in range(28124):
        if not findPairs(abundant_numbers, i):
            non_abundant_sum += i

    print(non_abundant_sum)

if __name__ == '__main__':
    main()