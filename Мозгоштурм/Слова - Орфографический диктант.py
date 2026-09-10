"""
  Суть этой задачи проста – просто перепеши слова без ошибок, однако я специально подобрал слова, которые даже сложно произнести 
"""
def lev(s1, s2):
    if len(s1) < len(s2):
        return lev(s2, s1)

    if len(s2) == 0:
        return len(s1)

    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row

    return previous_row[-1]

def letters_dictation():
    import random, sys
    letters = ["эквилибристика", "контрвзъём", "грхмцвакл", "мфломокпимпи", "гексакосиойгексеконтагексафобия", "бесперспективняк", "афродизиакотерапия", "каракалябаракалябушка", "меамеамеалоккабипуа", "всплескогеометризированный", "субстанционализирующимися", "человеконенавистничество", "гиппопотомонстросескипедалофобия", "интернационализирующимися", "фиброгастродуоденоскопия", "рекогносцировка", "взбалмошный", "короткошеее", "частнопредпринимательский", "дезоксирибонуклеиновая", "высокопревосходительство", "разглагольствовать", "гидроэлектростанциостроительство", "сверхпроводникообразующий", "контрреволюционизироваться", "противочеловеческоориентированный", "воспользовавшемуся", "выкристаллизовавшимися", "демуниципализировать", "превысокомногорассмотрительствующее", "росгпавстанкоинструментснабсбыт", "переподвыподвертом", "циклопентодиенилтрикарбонил"]
    randomLetter = random.choice(letters)
    
    riir = input(f"Напиши это слово без ошибок: {randomLetter} ")
    errors = lev(randomLetter.lower().strip(), riir.lower().strip())
    if errors > 0:
        print(f"   Ты написал слово за {errors} ошибок")
    elif errors == 0:
        print("   Ты написал слово абсолютно правильно")
        
    if riir == "_clear":
        sys.stdout.write("\033[2J\033[H")
        sys.stdout.flush()
    letters_dictation()
letters_dictation()
