"""
LeetCode 266 (Premium)
Given a string, determine if a permutation of the string could form a palindrome.
"""

def isPalindromePermutation(s: str) -> bool:
    ns = ""
    cont = 0
    for i in s:
        if i != " ":
            ns += i

    ns = ns.lower()

    x = set(ns)

    for j in x:
        y = ns.count(j)
        if  y % 2 != 0:
            cont += 1

        if cont > 1:
            return False
        
    return True

print(isPalindromePermutation("carerac"))