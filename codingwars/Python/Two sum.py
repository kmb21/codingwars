def two_sum(numbers, target):
    
    for num1 in range(len(numbers)-1):
        for num2 in range(num1+1, len(numbers)):
            sum = numbers[num1] + numbers[num2]
            if sum == target:
                return [num1, num2]