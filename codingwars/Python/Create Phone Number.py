def create_phone_number(n):
    number = '('
    for num1 in range(3):
        number += str(n[num1])
    number += ') '
    for num2 in range(3,6):
        number += str(n[num2])
    number += '-'
    for num3 in range(6,10):
        number += str(n[num3])
    return number