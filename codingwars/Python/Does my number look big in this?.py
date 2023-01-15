def narcissistic( value ):
    str_ver = str(value)
    sum = 0
    for i in str_ver:
        integer = int(i)
        sum += integer**len(str_ver)
    if sum == value:
        return True
    return False