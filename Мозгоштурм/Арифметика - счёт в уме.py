import math, random
from math import *
# В РАЗРАБОТКЕ

"""
   sqrt(x) – квадратный корень (x ^ 0.5)
   cbrt(x) – кубический корень числа (x ^ 0.(3))
   abs(x) – модуль числа (|x|, x ∈ R, x ≥ 0)
   fac(x) – факториал числа (x! = 1 × 2 × 3 × ... × x)
   dfac(x) – двойной факториал (x!! = ∏[n] | x ∈ N, 1 ≤ n ≤ x ∧ n % 2 == x % 2)
   log(x, n) – логарифм (logₐ(b) ⟺ a^x = b, x ∈ R, a ∈ (0;1) ∪ (1; +∞), b ∈ (0; +∞))
   summod(x) – сумма всех делителей (∑ [d ∈ {x∈N|x|n}] d)
"""

operat = globals().get("operations", 2)
charsj = globals().get("oper_chars", ["+", "-", "×", "//", "sqrt", "abs", "log"])
minum = globals().get("minnum", 0)
manum = globals().get("maxnum", 15)

def get_log_base(n):
    if n <= 1:
        return n
    base_factors = set()
    d = 2
    temp = n
    
    while d * d <= temp:
        if temp % d == 0:
            base_factors.add(d)
            while temp % d == 0:
                temp //= d
        d += 1
    if temp > 1:
        base_factors.add(temp)
    result_base = 1
    for factor in base_factors:
        result_base *= factor
    return result_base
    
def log(number, index):
    number = 1 if number == 0 else number
    index = 1 if index == 0 else index
    try:
       return math.log(number) / math.log(index)
    except ZeroDivisionError:
      return 1
    
def summod(n):
    return sum(i for i in range(1, n + 1) if n % i == 0)



def calculate(operations=operat, oper_chars=charsj, maxnum=manum, minnum=minum, **kwargs):
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
        if randomOper == "sqrt" or randomOper == "cbrt":
            rnmb = rnmb ** 2 if randomOper == "sqrt" else rnmb ** 3
            rnmb_oper = random.choice([char for char in oper_chars if char in '+-*/()'])
            randomNumber = f"{rnmb_oper} {randomOper}({rnmb}) "
        elif randomOper == "abs" or randomOper == "summod":
            rnmb_oper = random.choice([char for char in oper_chars if char in "+-*/()"])
            randomNumber = f"{rnmb_oper} {randomOper}({rnmb}) "
        elif randomOper == "log":
            rnmb_oper = random.choice([char for char in oper_chars if char in "+-*/()"])
            rnmb = rnmb ** 2
            randomIndex = get_log_base(rnmb)
            randomNumber = f"{rnmb_oper} {randomOper}({rnmb}, {randomIndex}) "
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
calculate(operat, charsj, manum, minum)
