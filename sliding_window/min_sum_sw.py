nums = [5, 4, 7, 1, 8]  # min sum of 3 consecutive numbers -> 12
n = len(nums)
k = 3

window_sum = sum(nums[:k])
min_sum = window_sum

for right in range(k, n):
    window_sum -= nums[right-k]
    window_sum += nums[right]

    min_sum = min(window_sum, min_sum)

print(min_sum)