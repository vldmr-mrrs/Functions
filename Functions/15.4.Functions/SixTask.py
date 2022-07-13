nums = input().split()


def cmp(num):
    n = [int(i) for i in num]
    print(n)
    return sum(n)


nums.sort(key=cmp)
print(*nums)
