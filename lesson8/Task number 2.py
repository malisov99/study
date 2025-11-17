l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))

numbers = set(l1).intersection(l2)

print(len(numbers))