def containsDuplicate(nums: [int]) -> bool:
    lista = set()

    for i in nums:
        if i in lista:
            return True
            
        lista.add(i)      
    return False   
    

x = [2,2,4,5]

print(containsDuplicate(x))