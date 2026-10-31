"""
   Это задачи с использованием эффекта Струпа. Пока что находится в разработке (второй режим)
"""
import sys, os
def rhemisphere_effstrupe():
    import random
    colors = {"красный": "91m", "оранжевый": "93m", "желтый": "93m", "зеленый": "92m", "голубой": "96m", "синий": "94m", "фиолетовый": "95m", "коричневый": "38;5;94m", "серый": "38;5;244m"}
    randomColor = random.choice(list(colors.keys())).upper()
    randomColorInt = random.choice(list(colors.values()))
    text = []
    text = f"\033[{randomColorInt}{randomColor}\033[0m"
    
    print(text, flush=True, end="")
    result = input(" ")
    if result.lower() in list(colors.keys()):
      print("   Это верно")
    elif result == "_QUIT" or result == "_EXIT":
      print("Завершение режима")
      sys.exit(0)
    elif result == "_CLEAR":
       try:
            os.system("clear")
        except Exception:
            os.system("cls")
    else:
       print("  Это не верно")
    rhemisphere_effstrupe()
rhemisphere_effstrupe()
