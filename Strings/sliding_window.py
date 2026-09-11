list = [2, 1, 5, 1, 3, 2]
list_len = len(list)

k = 3
window_sum = 0

# First window
for i in range(k):
    window_sum += list[i]

max_sum = window_sum

for right in range(k, list_len):
    window_sum -= list[right - k]
    window_sum += list[right]

    print(window_sum)

    max_sum = max(window_sum, max_sum)

print(max_sum)