def longest_common_prefix(strs):
    if not strs:
        return ""
    
    return lcp_recursive(strs, 0, len(strs) - 1)

def lcp_recursive(strs, left, right):
    if left == right:
        return strs[left]
    
    mid = (left + right) // 2
    left_lcp = lcp_recursive(strs, left, mid)
    right_lcp = lcp_recursive(strs, mid + 1, right)
    
    return common_prefix(left_lcp, right_lcp)

def common_prefix(str1, str2):
    min_len = min(len(str1), len(str2))
    for i in range(min_len):
        if str1[i] != str2[i]:
            return str1[:i]
    return str1[:min_len]

strs = ["flower", "flow", "flight"]
result = longest_common_prefix(strs)
print(f'O maior prefixo comum é: "{result}"')
