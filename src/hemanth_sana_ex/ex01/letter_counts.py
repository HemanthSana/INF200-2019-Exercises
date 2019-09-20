def letter_freq(txt):
    freq = {}
    for let in txt.lower():
        if let not in freq:
            freq[let] = 0
        freq[let] += 1
    return freq


if __name__ == '__main__':
    text = input('Please enter text to analyse: ')

    frequencies = letter_freq(text)
    for letter, count in frequencies.items():
        print('{:3}{:10}'.format(letter, count))
