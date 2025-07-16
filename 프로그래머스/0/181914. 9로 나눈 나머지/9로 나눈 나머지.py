def solution(number):
    sum = 0
    for i in number:
        sum += int(i)
    result = sum % 9
    return result