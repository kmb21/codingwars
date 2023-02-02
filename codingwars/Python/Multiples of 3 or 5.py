def solution(number):
    sum = 0
    if number < 0:
        return 0
    else:
        for num in range(number):
            if num%3 == 0 or num%5 ==0:
                sum += num
    return sum
  