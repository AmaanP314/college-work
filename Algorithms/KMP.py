def strStr(haystack: str, needle: str) -> int:
    if needle == '': return 0 
    m, n = len(haystack), len(needle)
    lps = [0] * n
    prevLPS, i = 0, 1
    while i < n:
        if needle[i] == needle[prevLPS]:
            lps[i] = prevLPS + 1
            prevLPS += 1
            i += 1
        elif prevLPS == 0:
            lps[i] = 0
            i += 1
        else:
            prevLPS = lps[prevLPS - 1]
    i, j = 0, 0
    while i < m:
        if haystack[i] == needle[j]:
            i, j = i+1, j+1
        elif j == 0:
            i += 1
        else:
            j = lps[j - 1]
        if j == n:
            return i - n
    return -1

haystack = "hello"
needle = "ll"
result = strStr(haystack, needle)
print(f"Index of first occurrence of '{needle}' in '{haystack}': {result}")  # Output: Index of first occurrence of 'll' in 'hello': 2