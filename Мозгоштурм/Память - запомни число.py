"""
   Просто запомни цифры и напиши их
   У меня, кстати, благодаря этому усилился эйдетизм, на удивление
"""

import os
def lev(s1, s2):
    matrix = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]
    
    for i in range(len(s1) + 1):
        matrix[i][0] = i
    for j in range(len(s2) + 1):
        matrix[0][j] = j
        
    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            if s1[i - 1] == s2[j - 1]:
                cost = 0
            else:
                cost = 1
                
            matrix[i][j] = min(
                matrix[i - 1][j] + 1,
                matrix[i][j - 1] + 1,
                matrix[i - 1][j - 1] + cost
            )
            
    return matrix[len(s1)][len(s2)]

def memory_digits(maxlen=10):
    import random
    nums = []
    
    for _ in range(1, maxlen + 1):
        nums.append(str(random.randint(0, 9)))
    nums = "".join(nums)
    
    text = f"Запомни эти цифры в скобках ({nums}). После того как ты нажмёшь нажмёшь, то этот текст исчезнет"
    print(text, end="", flush=True)
    input("")
    os.system("clear")
    
    result = input("\r" + " " * len(text) + "\rКакие цифры были до этого? ")
    if lev(result, nums) >= 1:
        print(f"Ты написал цифры с {lev(result, nums)} ошибками\n", end="", flush=True)
    else:
        print("Ты написал все цифры без ошибок\n", end="", flush=True)
    memory_digits(maxlen)
memory_digits(7)
