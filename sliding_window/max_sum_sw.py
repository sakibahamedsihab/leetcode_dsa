# sliding sindow
# list is given, need to find the maximum sum of 3 consecuitive elements in the list


nums = [2, 3, 1, 4, 5, 6, 7]
n = len(nums)
k = 3

# calculating the first window sum
window_sum = sum(nums[:k])
max_sum = window_sum

for right in range(k, n):
    # removing the left elelement, and adding the right element. So that the window slid
    window_sum -= nums[right - k]
    window_sum += nums[right]

    max_sum = max(window_sum, max_sum)

print(max_sum)
