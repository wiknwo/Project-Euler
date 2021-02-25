'''Problem 14: Longest Collatz Sequence

    William Ikenna-Nwosu (wiknwo)

    The following iterative sequence is defined for the set 
    of positive integers:

    n → n/2 (n is even)
    n → 3n + 1 (n is odd)

    Using the rule above and starting with 13, we generate 
    the following sequence:

    13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

    It can be seen that this sequence (starting at 13 and 
    finishing at 1) contains 10 terms. Although it has not 
    been proved yet (Collatz Problem), it is thought that 
    all starting numbers finish at 1.

    Which starting number, under one million, produces the 
    longest chain?

    NOTE: Once the chain starts the terms are allowed to go 
    above one million.
'''
def main():
    n = 1
    starting_number = 1
    sequence = [starting_number]
    count = 0
    longest_chain = 0
    starting_number_longest_chain = -1

    while starting_number < 1000000:
        if n == 1 and count != 0:
            if len(sequence) > longest_chain:
                longest_chain = len(sequence)
                starting_number_longest_chain = starting_number
            sequence.clear()
            starting_number += 1
            n = starting_number
            sequence.append(starting_number)
        elif n % 2 == 1:
            n = (3 * n) + 1
            sequence.append(n)
        elif n % 2 == 0:
            n = n / 2
            sequence.append(n)
        count += 1
        
    print(starting_number_longest_chain)
    print(longest_chain)
if __name__ == '__main__':
    main()