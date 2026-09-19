nums = [2, 3, 5, 6, 6, 8, 5, 3]
n = len(nums)
k = 3

even_count = 0

for i in range(k):
    if nums[i] % 2 == 0:
        even_count += 1

for right in range(k, n):
    if nums[right-k] % 2 == 0:
        even_count -= 1

    if nums[right] % 2 == 0:
        even_count += 1

print(even_count)