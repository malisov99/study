numbers = list(map(int, input().split()))

s = set()

for num in numbers:
    if num in s:
        print("YES")
    else:
        print("NO")
        s.add(num)