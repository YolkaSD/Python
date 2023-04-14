n = int(input())
min_weight = 30000
max_weight = 0

for i in range(n):
    weight = int(input())
    if weight > max_weight:
        max_weight = weight
    if weight < min_weight:
        min_weight = weight

print(min_weight, max_weight)
