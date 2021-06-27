N, A, B = map(int, input().split())
ans = 0

def FindSumOfDigits(x):
    count = 0
    while x > 0:
        count += x % 10
        x = x//10

    return count


for n in range(1, N+1):
    count = FindSumOfDigits(n)
    if A <= count <= B:
        ans += n
print(ans)