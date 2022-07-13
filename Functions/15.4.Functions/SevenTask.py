def comparator(numbers):
    n = [int(i) for i in numbers]
    return sum(n), int(numbers)


nums = input().split()
nums.sort(key=comparator)
print(*nums)