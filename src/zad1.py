

def check_candidates(names_input: str, scores_input: str )-> str:


    list_names_input = names_input.split(",") # Строку преобразовываем в список
    list_scores_input = scores_input.split("|") # Строку преобразовываем в список


    print(list_names_input)
    print(list_scores_input)

    check_candidates = []
    for names in list_names_input:

        index_names = list_names_input.index(names) # Получаем индекс

        scores = list_scores_input[index_names] # Получаем оценки по индексу

        list_scores = scores.split(",") # Преобразовываем оценки в список

        list_scores = [int(item) for item in list_scores] # Преобразовываем элементы списка в int



        if sum(list_scores)/ len(list_names_input) > 50:
            check_candidates.append(names)


    return ", ".join(check_candidates) # Преобразовываем список в строку


names_input = input()
scores_input = input()
result = check_candidates(names_input ,scores_input)
print(result)