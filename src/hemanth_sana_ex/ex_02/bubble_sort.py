def bubble_sort(sort_list):
    """
    Here we give data as input and get a sorted list as output
    """
    sorted_list = list(sort_list)
    for i in range(len(sorted_list)):
        for j in range(i, len(sorted_list)):
            if sorted_list[i] > sorted_list[j]:
                sorted_list[i], sorted_list[j] = sorted_list[j], sorted_list[i]
    return sorted_list


if __name__ == "__main__":

    for data in ((),
                 (1,),
                 (1, 3, 8, 12),
                 (12, 8, 3, 1),
                 (8, 3, 12, 1)):
        print('{!s:>15} --> {!s:>15}'.format(data, bubble_sort(data)))
