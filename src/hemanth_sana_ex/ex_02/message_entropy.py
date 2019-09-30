import math


def letter_freq(text):
    """
    letter_freq returns a dictionary with
    number of occurrences of each character
    """
    freq_dict = {}
    for letter in text.lower():
        if letter not in freq_dict:
            freq_dict[letter] = 0
        freq_dict[letter] += 1
    return freq_dict


def entropy(message):
    """
    entropy describes how difficult it is to guess-
                   individual letters in a message
    """
    frequency = letter_freq(message)
    sum_of_freq = len(message)
    entropy_sum = 0
    for i in frequency.keys():
        prob = frequency[i]/sum_of_freq
        entropy_sum = entropy_sum - sum([prob * math.log2(prob)])
    return entropy_sum


if __name__ == "__main__":
    for msg in '', 'aaaa', 'aaba', 'abcd', 'This is a short text.':
        print('{:25}: {:8.3f} bits'.format(msg, entropy(msg)))
