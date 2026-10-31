# в разработке
import sys, os

leve = globals().get("level", 1)

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
    
def anagrams_lv2(text):
    import re, random
    def shuffle_word(match):
        word = match.group(0)
        letters = list(word)
        random.shuffle(letters)
        return "".join(letters)
    return re.sub(r"[a-zA-Zа-яА-ЯёЁ]+", shuffle_word, text)
    

def letters_anagrams(level=leve):
    import random
    letters_lv1 = ["капибара", "утка", "русский", "большой", "цыган", "анаграмма", "программирование", "тренировка", "яблоко", "киви", "ягода", "вундеркинд", "яблоня", "груша", "клубника", "маленький", "колосальный", "гигант", "микроскопический", "автодидакт", "товар", "теремок", "маньяк", "птица", "цыплёнок", "перепонка", "катализатор", "фосфор", "компромис", "эрудиция", "мышцы", "анализ", "змея", "овощ", "деревяшка", "тетрадь", "кружка", "грифель", "электричество", "скобки", "чемодан", "шляпа", "фляга", "ягуар", "кровь", "крыша", "кладбище", "череп", "кость", "хохотать", "зевота", "символ", "подушка", "попугай", "кормушка", "клетка", "кружка", "тарелка", "книга", "наука", "розетка", "кровать", "простыня", "шкаф", "парта", "гантель", "штанга", "гриф",
    "попугай", "алфавит", "товарищ", "тумбочка", "электричество", "животное", "резина", "жесть", "политика", "лупа", "листья", "искривление", "аффикс"]
    letters_lv2 = ["мой дом", "гигантский подвал", "сложная анаграмма", "большая капибара", "умный автодидакт", "маленькая утка", "мастерский программист", "дорогой товар", "водный катализатор", "ускоритель частиц", "белый фосфор", "титановая пластина", "много яблок", "корень числа", "пластмассовая бутылка", "водная гладь", "сильная мышца"]
    
    randomWord = ""
    anogram = ""
    if level <= 1:
        randomWord = random.choice(letters_lv1)
        anogram = "".join(random.sample(randomWord, len(randomWord)))
    elif level == 2:
        randomWord = random.choice(letters_lv2)
        anogram = anagrams_lv2(randomWord)
    result = input(f"Какое слово здесь спрятано: {anogram} ")
    
    if lev(randomWord, result) >= 1:
        print(f"   Ты написал слово за {lev(randomWord, result)} ошибок. Оригинальное слово было '{randomWord}'")
    elif result == "_QUIT" or result == "_EXIT":
        print("Завершение режима")
        sys.exit(0)
    elif result == "_CLEAR":
        try:
            os.system("clear")
        except Exception:
            os.system("cls")
    else:
        print("   Ты написал слово без ошибок")
    letters_anagrams(level)
letters_anagrams(leve)
