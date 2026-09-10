def longest_substring(text: str) -> int:
    n = len(text)
    max_len = 0

    for start in range(n):
        seen = set()

        for end in range(start, n):
            char = text[end]

            if char in seen:
                break

            seen.add(char)
            current_len = end - start + 1
            max_len = max(current_len, max_len)

    return max_len

