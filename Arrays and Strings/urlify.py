"""
Not Found in LeetCode
Write a method to replace all spaces in a
string with '%20'
"""

def URLify(s: str):
    ns = ""
    for i in s:
        if i != " ":
            ns = ns + i
        else:
            ns = ns + "%20"
            
    print(ns)

URLify("Hola")