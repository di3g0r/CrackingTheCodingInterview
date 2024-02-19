"""
LeetCode 443 (Medium)

"""

def compress(chars: [str]) -> int:
    char = chars[0]
    cont = 0
    master_cont = 0
    original_len = len(chars)
    index = 0

    s = ""

    for i in chars:
        index += 1

        if i  == char:
            cont+=1

        if i != char or original_len == index:
            if cont == 1:
                s += char
                master_cont +=1

            else:
                s += char
                x = str(cont)
                s += x
                master_cont += (len(x) + 1)

                """elif cont >= 10:
                string_num = str(cont)
                s += char
                master_cont +=1

                for j in string_num:
                    s += j
                    master_cont +=1
                    x+=1""" 

            if index == original_len:
                print(s)
                print(master_cont)
                return master_cont
            
            char = chars[index-1]
            cont = 1


    print(s)
    print(master_cont)
    return master_cont

chars = ["a","a","b","b","c","c","c"]
compress(chars)