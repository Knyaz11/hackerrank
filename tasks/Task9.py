def sockMerchant(n, ar):
    counts = {}
    for sock in ar:
        counts[sock] = counts.get(sock, 0) + 1
    
    pairs = 0
    for count in counts.values():
        pairs += count // 2
    
    return pairs

n = int(input())
ar = list(map(int, input().split()))
print(sockMerchant(n, ar))
