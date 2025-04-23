def longestCommonSubsequence(text1: str, text2: str) -> int:
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if text1[i] == text2[j]:
                dp[i][j] = 1 + dp[i + 1][j + 1]
            else:
                dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])
    return dp[0][0]

text1 = "abcde"
text2 = "ace"
result = longestCommonSubsequence(text1, text2)
print(f"Length of Longest Common Subsequence: {result}")  # Output: Length of Longest Common Subsequence: 3


#OPTIONAL TO ALSO PRINT THE STRING:
def longestCommonSubsequence(text1: str, text2: str) -> tuple:
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Fill the DP table
    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if text1[i] == text2[j]:
                dp[i][j] = 1 + dp[i + 1][j + 1]
            else:
                dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])
    
    # Reconstruct the LCS string
    lcs = []
    i, j = 0, 0
    while i < m and j < n:
        if text1[i] == text2[j]:
            lcs.append(text1[i])
            i += 1
            j += 1
        elif dp[i + 1][j] >= dp[i][j + 1]:
            i += 1
        else:
            j += 1
    
    return dp[0][0], ''.join(lcs)

# Test the function
text1 = "abcde"
text2 = "ace"
length, lcs_string = longestCommonSubsequence(text1, text2)
print(f"Length of Longest Common Subsequence: {length}")
print(f"Longest Common Subsequence: {lcs_string}")
