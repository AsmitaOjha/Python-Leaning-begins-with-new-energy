def sum_eo(n, t):
    sum_result = 0
    
    if t == 'e':
        for i in range(0, n, 2):
            sum_result += i
    elif t == 'o':
        for i in range(1, n, 2):
            sum_result += i
    
    return sum_result

result = sum_eo(8, 'e')
print(result)