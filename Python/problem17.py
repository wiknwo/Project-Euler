'''Problem 17

    William Ikenna-Nwosu (wiknwo)

    If the numbers 1 to 5 are written out in words: one, 
    two, three, four, five, then there are 3 + 3 + 5 + 4 + 
    4 = 19 letters used in total.

    If all the numbers from 1 to 1000 (one thousand) 
    inclusive were written out in words, how many letters 
    would be used?

    NOTE: Do not count spaces or hyphens. For example, 342 
    (three hundred and forty-two) contains 23 letters and 
    115 (one hundred and fifteen) contains 20 letters. The 
    use of "and" when writing out numbers is in compliance 
    with British usage.
'''
def to_letter_count(number):
    '''Function to convert number to letter count 

        Args:
            number(int): number

        Raises:

        Return:
            lettercount(int): lettercount
    '''
    UNITS = ['one', 'two', 'three', 'four', 'five', 'six',
             'seven', 'eight', 'nine', 'ten', 'eleven', 
             'twelve', 'thirteen', 'fourteen', 'fifteen',
             'sixteen', 'seventeen', 'eighteen', 'nineteen']
    TENS = ['twenty', 'thirty', 'forty', 'fifty', 'sixty',
            'seventy', 'eighty', 'ninety']
    HUNDREDS = ['hundred']
    THOUSAND = ['thousand'] 
    lettercount = 0

    if number < 20:
        lettercount += len(UNITS[number - 1])
    elif number >= 20 and number <= 99:
        if number % 10 == 0:
            lettercount += len(TENS[(number // 10) - 2])
        else:
            lettercount += len(TENS[(number // 10) - 2]) + len(UNITS[(number % 10) - 1])
    elif number >= 100 and number <= 999:
        if number % 100 == 0:
            lettercount += len(UNITS[(number // 100) - 1]) + len(HUNDREDS[0])
        else:
            lettercount += len(UNITS[(number // 100) - 1]) + len(HUNDREDS[0]) + len('and') + to_letter_count(number % 100)
    elif number == 1000:
        lettercount += len(UNITS[0]) + len(THOUSAND[0])
    return lettercount

def main():
    lettercount = 0

    for i in range(1, 1001):
        lettercount += to_letter_count(i)
    print(lettercount)
    
if __name__ == '__main__':
    main()
