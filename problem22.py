'''Problem 22: Names Scores

    William Ikenna-Nwosu (wiknwo)

    Using names.txt (right click and 'Save Link/Target 
    As...'), a 46K text file containing over five-thousand 
    first names, begin by sorting it into alphabetical 
    order. Then working out the alphabetical value for 
    each name, multiply this value by its alphabetical 
    position in the list to obtain a name score.

    For example, when the list is sorted into 
    alphabetical order, COLIN, which is worth 3 + 15 + 
    12 + 9 + 14 = 53, is the 938th name in the list. So, 
    COLIN would obtain a score of 938 × 53 = 49714.

    What is the total of all the name scores in the file?
'''
import string

def main():
    letters_dict = dict(zip(string.ascii_uppercase, range(1,27)))
    data = []
    total_names_scores = 0
    with open('names.txt', 'r') as f:
        for line in f:
            data = line.replace('"', '').rstrip().split(",")

    data.sort() # Sort names first

    # Calculate total naems scores
    for i in range(len(data)):
        name_score = 0
        for char in data[i]:
            name_score += letters_dict[char]
        name_score *= (i + 1)
        total_names_scores += name_score
        # if data[i] == 'COLIN':
        #     print('{} {}'.format(i + 1, name_score))
    print(total_names_scores)
        
if __name__ == '__main__':
    main()