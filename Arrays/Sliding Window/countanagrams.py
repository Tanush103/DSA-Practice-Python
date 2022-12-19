# Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
# typically using all the original letters exactly once.

 

# Example 1:

# Input: s = "cbaebabacd", p = "abc"
# Output: [0,6]
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
# Example 2:

# Input: s = "abab", p = "ab"
# Output: [0,1,2]
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".

from collections import Counter
def startindicesofanagrams(s,p):
    hash_p=dict(Counter(p))
    hash_s=Counter(s)
    arr=[]
    i=0
    count=0
    len1=len(hash_p)
    for j in range(len(s)):
        if s[j] in hash_p:
            hash_p[s[j]]-=1
            if hash_p[s[j]]==0:
                len1-=1
        if j-i+1==len(p):
            if len1==0:
                count+=1
                arr.append(i)
            if s[i] in hash_p:
                hash_p[s[i]]+=1
                if hash_p[s[i]]==1:
                    len1+=1
            i+=1
    return arr


print(startindicesofanagrams("cbaebabacd","abc"))  



