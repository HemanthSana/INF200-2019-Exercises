import io


def char_counts(input_file_name):
    """
    Returns a list with the frequency of each-
       letter with utf-8 encoding
    """
    utf_list = [0] * 256
    with io.open(input_file_name, 'r', encoding='utf8') as file:
        file_content = file.read().rstrip("\n")
        for char in file_content:
            utf_code = ord(char)
            utf_list[utf_code] += 1
    return utf_list


if __name__ == '__main__':

    filename = 'file_stats.py'
    frequencies = char_counts(filename)
    for code in range(256):
        if frequencies[code] > 0:
            character = ''
            if code >= 32:
                character = chr(code)

            print(
                '{:3}{:>4}{:6}'.format(
                    code, character, frequencies[code]
                )
            )
