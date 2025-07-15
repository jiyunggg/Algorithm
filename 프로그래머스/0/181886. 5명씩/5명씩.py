def solution(names):
    first_name_group = []
    for i in range(0, len(names), 5):
        sliced_group = names[i:i+5]
        first_name_group.append(sliced_group[0])
    return first_name_group    
        