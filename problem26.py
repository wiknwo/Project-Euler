'''Problem 26: Reciprocal Cycles

    William Ikenna-Nwosu (wiknwo)

    A unit fraction contains 1 in the numerator. The 
    decimal representation of the unit fractions with 
    denominators 2 to 10 are given:

    1/2	= 	0.5
    1/3	= 	0.(3)
    1/4	= 	0.25
    1/5	= 	0.2
    1/6	= 	0.1(6)
    1/7	= 	0.(142857)
    1/8	= 	0.125
    1/9	= 	0.(1)
    1/10	= 	0.1

    Where 0.1(6) means 0.166666..., and has a 1-digit 
    recurring cycle. It can be seen that 1/7 has a 
    6-digit recurring cycle.

    Find the value of d < 1000 for which 1/d contains the 
    longest recurring cycle in its decimal fraction part. 
'''   
def main():
    # longest_recurring_cycle_length = -1
    # unit_fraction = 0
    # recurring_decimals = []
    # denominator = 0

    # for d in range(999, 1, -1):
    #     unit_fraction = str(1 / d)
    #     for char in unit_fraction:
    #         if char not in recurring_decimals:
    #             recurring_decimals.append(char)
    #         else:
    #             recurring_decimals.append(char)
    #             if recurring_decimals.count(char) > 2:
    #                 break
    #     if len(recurring_decimals) > longest_recurring_cycle_length:
    #         longest_recurring_cycle_length = len(recurring_decimals)
    #         denominator = d
    #     recurring_decimals.clear()
    #     print(unit_fraction)
    # print(longest_recurring_cycle_length)
    # print(denominator)
    longest_recurring_cycle_length = 0
    longest_recurring_cycle_denominator = 0
    
    for d in range(999, 0, -1):
        quotient = {0 : 0} # Stores the decimal quotient
        current_value = 1  # Variable used to perform division as if by hand
        recurring_decimal_length = 0

        # Perform division as if by hand
        while current_value not in quotient: # while the value is not recurring
            recurring_decimal_length += 1
            quotient[current_value] = recurring_decimal_length
            current_value = (current_value % d) * 10

        if not current_value:
            continue

        # Remove number of values that do not recur
        recurring_decimal_length -= quotient[current_value]

        if recurring_decimal_length > longest_recurring_cycle_length:
            longest_recurring_cycle_length = recurring_decimal_length
            longest_recurring_cycle_denominator = d
    print('Longest recurring cycle length: {}'.format(longest_recurring_cycle_length))
    print('Longest recurring cycle denominator: {}'.format(longest_recurring_cycle_denominator))
    
if __name__ == '__main__':
    main()