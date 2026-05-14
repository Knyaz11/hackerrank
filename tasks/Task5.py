def getTotalX(a, b):
    count = 0

    for x in range(max(a), min(b) + 1):
        if all(x % i == 0 for i in a):
            if all(j % x == 0 for j in b):
                count += 1

    return count


n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

print(getTotalX(a, b))
