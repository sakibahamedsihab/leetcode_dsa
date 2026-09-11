nums = [2, 6, 3, 4, 1, 4, 3]
n = len(nums)
k = 3

window_sum = sum(nums[:k])
max_sum = window_sum

for right in range(k, n):
    window_sum -= nums[right-k]
    window_sum += nums[right]

    max_sum = max(window_sum, max_sum)

max_avg = max_sum / k
print(f'Maximum sum: {max_sum}')

print(f'Maximum average: {max_avg}')