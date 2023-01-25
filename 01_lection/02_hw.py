n, i, j = list(map(int, input().split(' ')))

if i < j:
    left = j - i - 1
    right = n - j - 1 + i
else:
    left = i - j - 1
    right = n - i - 1 + j

if left < right:
    print(left)
else:
    print(right)
