def sum_of_divisible_naturals(limit):
    total = 0
    for n in range(1, limit):
        if n % 3 == 0 or n % 5 == 0:
            total = total + n
    return total

if '__name__' == '__main__':
    print(sum_of_divisible_naturals(1000))
