# в разработке
import random, infinite_math, os
def is_any_power(n):
    if n <= 0:
        return False
    if n == 1:
        return True
       
    for k in range(2, 11 + n // 1000):
        x = round(n ** (1 / k))
        if x ** k == n:
            return True
    return False
    
def is_repdigit(n):
    return len(set(str(n))) == 1
    
def math_classification(maxnum=1e4):
    a = "Является ли это число чётным: "
    b = "Является ли это число нечётным: "
    c = "Является ли это число простым: "
    d = "Является ли это число полиндромом: "
    e = "Является ли это число составным: "
    f = "Является ли это число совершенным: "
    g = "Является ли это число треугольным: "
    h = "Является ли это число избыточным: "
    i = "Является ли это число результатом любой степени: "
    j = "Является ли это число репдиджитом: "
    #Сфеническим
    #Полнократным
    #Прямоугольным
    #Бесквадратным
    #Полупростым
    #Частью последовательности Фибоначчи
    #Частью последовательности Каталана
    #числом Нивена
    
    newJek = (a, b, c, d, e, f, g, h, i, j)
    randomMode = random.choice(newJek)
    randomNumber = random.randint(0, int(maxnum))
    example = input(randomMode + str(randomNumber) + "? ")
    
    if randomMode == a:
        if (randomNumber % 2 == 0 and example == "1") or (randomNumber % 2 != 0 and example == "0"):
            print("   Это верно")
        else:
            print("   Это не верно")
    elif randomMode == b:
        if (randomNumber % 2 == 1 and example == "1") or (randomNumber % 2 == 0 and example == "0"):
            print("   Это верно")
        else:
            print("   Это не верно")
    elif randomMode == c:
        if (infinite_math.is_prime(randomNumber) and example == "1") or (not infinite_math.is_prime(randomNumber) and example == "0"):
           print("   Это верно")
        else:
           print("   Это не верно")
    elif randomMode == d:
        if (str(randomNumber) == str(randomNumber)[::-1] and example == "1") or (not str(randomNumber) == str(randomNumber)[::-1] and example == "0"):
            print("   Это верно")
        else:
            print("   Это не верно")
    elif randomMode == e:
        if (infinite_math.is_composite(randomNumber) and example == "1") or (not infinite_math.is_composite(randomNumber) == "0"):
            print("   Это верно")
        else:
            print("   Это не верно")
    elif randomMode == f:
        if (infinite_math.is_perfect(randomNumber) and example == "1") or (not infinite_math.is_perfect(randomNumber) == "0"):
            print("   Это верно")
        else:
            print("   Это не верно")
    elif randomMode == g:
         if (infinite_math.is_triangular(randomNumber) and example == "1") or (not infinite_math.is_triangular(randomNumber) == "0"):
            print("   Это верно")
         else:
            print("   Это не верно")
    elif randomMode == h:
         if (infinite_math.is_abundant(randomNumber) and example == "1") or (not infinite_math.is_abundant(randomNumber) and example == "0"):
             print("   Это верно")
         else:
             print("   Это не верно")
    if randomMode == i:
         if (is_any_power(randomNumber) and example == "1") or (not is_any_power(randomNumber) and example == "0"):
            print("   Это верно")
         else:
            print("   Это не верно")
    if randomMode == j:
        if (is_repdigit(j) and example == "1") or (not is_repdigit(j) and example == "0"):
            print("   Это верно")
        else:
            print("   Это не верно")
    if example == "_CLEAR":
        try:
            os.system("clear")
        except Exception:
            os.system("cls")
        print("\033[H\033[J", end="")
        
    math_classification(maxnum)
math_classification(1000)
