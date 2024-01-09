"""
LeetCode 242
Given two strings s and t, return true
if t is an anagram of s, and false otherwise.
"""

from collections import defaultdict

def isAnagram(s: str, t: str) -> bool:
    cont = defaultdict(int)

    for i in s:
        cont[i] += 1

    for j in t:
        cont[j] -= 1

    for x in cont.values():
        if x != 0:
            return False

    return True   

print(isAnagram("hola","aloh"))
print(isAnagram("hola","java"))