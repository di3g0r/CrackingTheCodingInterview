"""
LeetCode 217
Given an integer array nums, return true if any value
appears at least twice in the array, and return false if 
every element is distinct.
"""

def containsDuplicate(nums: [int]) -> bool:
    lista = set()

    for i in nums:
        if i in lista:
            return True
            
        lista.add(i)      
    return False   
    

x = [2,2,4,5]

print(containsDuplicate(x))