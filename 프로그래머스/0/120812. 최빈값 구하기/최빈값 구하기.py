def solution(array):
    count_size = max(array) + 1
    num_occ_array = [0] * count_size

    for i in array:
        num_occ_array[i] += 1

    max_num_occ = 0
    for i in num_occ_array:
        if i > max_num_occ:
            max_num_occ = i

    max_count_numbers = []
    for i in range(len(num_occ_array)):
        if num_occ_array[i] == max_num_occ:
            max_count_numbers.append(i)

    if len(max_count_numbers) > 1:
        return -1
    else:
        return max_count_numbers[0]