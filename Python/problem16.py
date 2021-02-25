'''Problem 16

    William Ikenna-Nwosu (wiknwo)

    2^15 = 32678 and the sum of its digits is 3 + 2 + 7 + 6 
    + 8 = 26.

    What is the sum of the digits of the number 21000?
'''
def main():
    number = str(2**1000)
    runningsum = 0
    for char in number:
        runningsum += int(char)
    print(runningsum)

if __name__ == '__main__':
    main()