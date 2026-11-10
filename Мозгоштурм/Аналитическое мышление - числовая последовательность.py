import random, sys, os

visib = globals().get("visible_count", 5)

def generate_sequence(length_visible):
    total_length = length_visible + 1
    start = random.randint(1, 10)
    types = ['arithmetic', 'geometric', 'squares', 'cubes', 'fibonacci', 'alternating', "placu", "xaca", "alph", "caca", "yh", "abab", "ftt", "fek", "irl", "jjd"]
    #types = ["jjd"]
    seq_type = random.choice(types)
    
    seq = []
    
    if seq_type == 'arithmetic':
        step = random.randint(-9, 9)
        seq = [start + i * step for i in range(total_length)]
        
    elif seq_type == 'geometric':
        step = random.randint(2, 4)
        start = random.randint(1, 3)
        seq = [start * (step ** i) for i in range(total_length)]
        
    elif seq_type == 'squares':
        start_idx = random.randint(1, 5)
        seq = [(i + start_idx) ** 2 for i in range(total_length)]
        
    elif seq_type == 'cubes':
        start_idx = random.randint(1, 9)
        seq = [(i + start_idx) ** 3 for i in range(total_length)]
        
    elif seq_type == 'fibonacci':
        a, b = random.randint(1, 9), random.randint(1, 9)
        seq = [a, b]
        for _ in range(total_length - 2):
            seq.append(seq[-1] + seq[-2])
            
    elif seq_type == "yh":
         start_idx = random.randint(1, 9)
         seq = [start_idx + i * 2 for i in range(total_length)]
         
    elif seq_type == "abab":
          start_idx = random.randint(1, 9)
          seq = [start_idx + (-1) ** i for i in range(total_length)]
          
    elif seq_type == "ftt":
          start_idx = random.randint(1, 9)
          seq = [start_idx * ((-1) ** i * 2 * i) for i in range(total_length)]
          
    elif seq_type == "fek":
          start_idx = random.randint(1, 9)
          seq = [start_idx + (i ** 2 - i + 1) for i in range(total_length)]
          
    elif seq_type == "irl":
          start_idx = random.randint(1, 9)
          seq = [start_idx + (i ** 2 - i * (start_idx // 2)) for i in range(total_length)]
          
    elif seq_type == "jjd":
          start_idx = random.randint(1, 9)
          seq = [start_idx + (i * (i + start_idx) // 2) for i in range(total_length)]
            
    elif seq_type == "placu":
        start_idx = random.randint(1, 9)
        seq = [start_idx + i for i in range(total_length)]
        
    elif seq_type == "xaca":
        start_idx = random.randint(1, 9)
        seq = [(start_idx * i) // 2 for i in range(total_length)]
        
    elif seq_type == "alph":
        start_idx, b = random.randint(1, 9), random.randint(2, 9)
        seq = [(start_idx + i) * b / 2 for i in range(total_length)]
        
    elif seq_type == "caca":
        start_idx = random.randint(1, 9)
        seq = [start_idx + i * i for i in range(total_length)]
        
    elif seq_type == 'alternating':
        step1 = random.randint(2, 5)
        step2 = random.randint(1, 3)
        current = start
        seq.append(current)
        for i in range(total_length - 1):
            if i % 2 == 0:
                current += step1
            else:
                current -= step2
            seq.append(current)
    return seq


def play_analytical_game(visible_count=visib):
    print("Угадайте следующее число в ряду. Для выхода введите 'выход' \n")
    
    while True:
        sequence = generate_sequence(visible_count)
        visible_part = sequence[:-1]
        correct_answer = sequence[-1]
        sequence_str = ", ".join(map(str, visible_part))
        
        print(f"Последовательность: {sequence_str}, ?")
        user_input = input("Ваш ответ: ").strip()
        
        if user_input.lower() in ['выход', 'exit', 'quit']:
            print(f"\nИгра окончена! Ваш итоговый счет: {score}")
            break
            sys.exit(0)
        elif user_input.lower() in ["cls", "clear"]:
            try:
                os.system("clear")
            except Exception:
                os.system("cls")
            
        try:
            if user_input == str(correct_answer):
                print("Это правильно")
            else:
                print(f"Неверно. Правильный ответ: {correct_answer}")
        except ValueError:
            print(f"Это неверно. Правильный ответ: {correct_answer}")

play_analytical_game(visible_count=visib)
