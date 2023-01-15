def sum_two_smallest_numbers(numbers):
    #your code here
    min = numbers[0] + numbers[1]
    for num1 in numbers:
        for num2 in numbers:
            if num1 != num2:
                max = num1 + num2
                if max < min:
                    min = max
    return min