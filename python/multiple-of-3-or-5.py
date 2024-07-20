def is_divisor_of_3_or_5(num):
    if num == 0:
        return False
    return num % 3 == 0 or num % 5 == 0

def get_sum_of_3_or_5(num):
    i = 0
    sum = 0

    while(num > i):

        if is_divisor_of_3_or_5(i):
            sum += i

        i += 1

    return sum


def get_sum_of_3_or_5_recursive(num, i=0):
    if num <= i:
        return 0
    
    if is_divisor_of_3_or_5(i):
        return i + get_sum_of_3_or_5_recursive(num, i + 1)


    return get_sum_of_3_or_5_recursive(num, i + 1)

