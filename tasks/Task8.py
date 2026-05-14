def migratoryBirds(arr):
    count = {}

    for bird in arr:
        if bird in count:
            count[bird] += 1
        else:
            count[bird] = 1

    max_count = max(count.values())

    result = min(bird for bird in count if count[bird] == max_count)

    return result


n = int(input())
arr = list(map(int, input().split()))

print(migratoryBirds(arr))
