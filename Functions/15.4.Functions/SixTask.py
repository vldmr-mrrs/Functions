def cmp(num):
    n = [int(i) for i in num]
    return sum(n)


nums = input().split()
nums.sort(key=cmp)
print(*nums)
