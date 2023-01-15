def square_digits(num):
    result = ''
    str_ver = str(num)
    for char in str_ver:
        result += str(int(char)**2)
        
    return int(result)