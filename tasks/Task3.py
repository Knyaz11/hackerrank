def countApplesAndOranges(s, t, a, b, apples, oranges):
    apple_count = 0
    orange_count = 0

    for d in apples:
        if s <= a + d <= t:
            apple_count += 1

    for d in oranges:
        if s <= b + d <= t:
            orange_count += 1

    print(apple_count)
    print(orange_count)


if __name__ == "__main__":
    s, t = map(int, input().split())
    a, b = map(int, input().split())
    m, n = map(int, input().split())

    apples = list(map(int, input().split()))
    oranges = list(map(int, input().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
