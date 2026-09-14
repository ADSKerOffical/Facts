import math, random
from math import *
# В РАЗРАБОТКЕ

"""
   sqrt(x) – квадратный корень (x ^ 0.5)
   cbrt(x) – кубический корень числа (x ^ 0.(3))
   abs(x) – модуль числа (|x|, x ∈ R, x ≥ 0)
   fac(x) – факториал числа (x! = 1 × 2 × 3 × ... × x)
   dfac(x) – двойной факториал (x!! = ∏[n] | x ∈ N, 1 ≤ n ≤ x ∧ n % 2 == x % 2)
   logₙ(x) – логарифм (logₐ(b) ⟺ a^x = b, x ∈ R, a ∈ (0;1) ∪ (1; +∞), b ∈ (0; +∞))
   summod(x) – сумма всех делителей (∑ [d ∈ {x∈N|x|n}] d)
"""

def calculate(operations=2, oper_chars=["+", "-", "×", "//", "sqrt", "abs"], maxnum=15, minnum=0, **kwargs):
    operations = kwargs.get("operations", operations)
    oper_chars = kwargs.get("oper_chars", oper_chars)
    maxnum = kwargs.get("maxnum", maxnum)
    minnum = kwargs.get("minnum", minnum)
    
    example = []
    startNum = str(random.randint(minnum, maxnum)) + " "
    example.append(startNum)
    
    for _ in range(0, operations):
        randomOper = random.choice(oper_chars)
        rnmb = random.randint(minnum, maxnum)
        if randomOper == "÷" or randomOper == "/" or randomOper == "//":
            rnmb = max(1, min(rnmb, maxnum))
        if randomOper == "sqrt":
            rnmb = rnmb ** 2
            rnmb_oper = random.choice([char for char in oper_chars if char in '+-*/()'])
            randomNumber = f"{rnmb_oper} {randomOper}({rnmb}) "
        elif randomOper == "abs":
            rnmb_oper = random.choice([char for char in oper_chars if char in "+-*/()"])
            randomNumber = f"{rnmb_oper} {randomOper}({rnmb}) "
        else:
            randomNumber = randomOper + " " + str(rnmb) + " "
        example.append(randomNumber)
        
    exm = "".join(example)
    answer = round(eval(exm.replace("×", "*").replace("÷", "/").replace("sqrt", "math.sqrt")), 2)
    if not isinstance(answer, int) and isinstance(answer, (float, complex)) and answer == int(answer):
        answer = int(answer)
    result = input(f"Сколько будет {exm}? ")
    
    if result == str(answer):
        print("   Это правильно")
    else:
        print(f"   Это не правильно, правильный ответ: {answer}")
    calculate(operations, oper_chars, maxnum, minnum)
calculate(3, minnum = -10)
