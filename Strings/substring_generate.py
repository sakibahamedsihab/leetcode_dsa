str = 'abcabcbb'
n = len(str)

for start in range(n):
    for end in range(start, n):
        print(str[start:end+1])
