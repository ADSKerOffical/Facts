"""
   Это задачи с использованием эффекта Струпа. Пока что находится в разработке (второй режим)
"""

def rhemisphere_effstrupe(level=1):
    import random
    colors = {"красный": "91m", "оранжевый": "93m", "желтый": "93m", "зеленый": "92m", "голубой": "96m", "синий": "94m", "фиолетовый": "95m", "коричневый": "38;5;94m", "серый": "38;5;244m"}
    randomColor = random.choice(list(colors.keys())).upper()
    randomColorInt = random.choice(list(colors.values()))
    text = []
    
    if level <= 1:
       text = f"\033[{randomColorInt}{randomColor}\033[0m"
    elif level == 2:
        iteration = 1
        while iteration <= 10:
            iteration += 1
            randomColor = random.choice(list(colors.keys())).upper()
            randomColorInt = random.choice(list(colors.values()))
            text.append(f"\033[{randomColorInt}{randomColor}\033[0m")
        text = " ".join(text)
    print(text, flush=True, end="")
    result = input(" ")
    if level == 1:
       if result.lower() in list(colors.keys()):
          print("   Это верно")
    elif level == 2:
       if result:
          print("   Это не верно")
    rhemisphere_effstrupe(level)
rhemisphere_effstrupe()
