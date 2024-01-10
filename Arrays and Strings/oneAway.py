"""
LeetCode 161 (Premium)
Given two strings write a function to check if they
are 1 or 0 edits away from being equal.
Example
pale, ple -> True
pale, bake -> False
"""

def oneEditAway(s: str, t: str) -> bool:

    dif = abs(len(s) - len(t))
    if dif > 1:
        return False
    
    cont = 0
    
    if len(s) == len(t):
        for i in range(0,len(s)):
            if s[i] != t[i]:
                cont += 1
            
            if cont > 1:
                return False
        
        return True
    
    if len(s) != len(t):
        wordS: []
        wordT: []
        j = 0

        if len(s) < len(t):
            while s[j] == t[j]:
                j += 1
                if j == len(s):
                    return True

            while j < len(s):
                if s[j] != t[j+1]:
                    return False
                j+=1  

            return True

        if len(t) < len(s):  
           while s[j] == t[j]:
                j += 1
                if j == len(t):
                    return True

           while j < len(t):
                if t[j] != s[j+1]:
                    return False
                j+=1  

           return True       


print(oneEditAway("pale","pale"))
print(oneEditAway("pa","pale"))
print(oneEditAway("pales","pale"))
print(oneEditAway("pale","pales"))
print(oneEditAway("pale","pasle"))
print(oneEditAway("pabes","pale"))
                

                       
            