# Count Prefix and Suffix
def countPrefixSuffixPairs(words):
    def isPrefixandSuffix(s1,s2):
        #Check if s2 has s1 as Prefix and Suffix
        return s2.startswith(s1) and s2.endswith(s1)

    count = 0
    n = len(words)
    for i in range(n):
        for j in range(i + 1, n): 
            # Ensure i<j
            if isPrefixandSuffix(words[i], words[j]):
                count += 1
    return count

words = ["a","aba","ababa","aa"]
print(countPrefixSuffixPairs(words))