def even_fibonacci_sum(limit = 100):
    a, b = 0, 1
    sum = 0
    while(a <= limit):
        if a % 2 == 0:
            sum += a
        a, b = b, a + b
   
    return sum

print(even_fibonacci_sum())