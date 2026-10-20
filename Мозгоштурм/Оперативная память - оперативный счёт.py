# В разработке
def numbers_opercount(interval=1, opers=5, maxnum=15, minnum=0):
    import random, os, time
    def clear():
        try:
            os.system("clear")
        except Exception:
            os.system("cls")
            
    example = []
    input("Нажми пробел когда будешь готов")
    randomNumber = str(random.randint(minnum, maxnum))
    operations = ["+", "-"]
    example.append(randomNumber)
    
    print(randomNumber)
    for _ in range(1, opers + 1):
        time.sleep(interval)
        clear()
        randomOper = random.choice(operations)
        randomNumber = str(random.randint(minnum, maxnum))
        exm = f"{randomOper}{randomNumber}"
        example.append(exm)
        print(exm)
    result = input("Какой результат? ")
    exmpl = str(eval("".join(example).replace(" ", "")))
    
    if result == exmpl:
        print("   Это правильный ответ")
    else:
        print(f"   Это не правильный ответ. Правильный ответ: {exmpl}")
    numbers_opercount(interval, opers, maxnum, minnum)
numbers_opercount(1)
