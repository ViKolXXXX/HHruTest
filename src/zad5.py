# Преподаватель отправил студентам ведомости с оценками за экзамен. Определите, удалось ли всем студентам в группе
# набрать проходной балл или выше. Проходной балл — 35. Если есть студенты, которые не набрали проходной балл,
# выведите их имена. Формат ввода Первая строка: целые числа, разделенные запятыми, означающие баллы учеников (1 ≤ x
# ≤ 55). Вторая строка: имена учеников, также разделенные запятыми. Гарантируется, что число баллов равно числу имен
# учеников. Формат вывода Одна строка: «Все сдали», если все ученики набрали баллы 35 и выше. В противном случае —
# «Есть не сдавшие» (обе фразы без кавычек), а на следующих строках вывести имена студентов, которые не сдали. Пример
# 1 Входные данные: 30,40,20 Alice,Bob,Charlie Выходные данные: Есть не сдавшие Alice Charlie Пример 2 Входные
# данные: 40,40,40 Mark,Jack,Jimmy Выходные данные: Все сдали


def check_all_students_passed(scores_input: str,names_input: str )-> str:
    """Ваш код"""
    scores = scores_input.split(',')
    scores_int = [int(item) for item in scores]
    names = names_input.split(',')
    not_pass = list()

    for i in range(len(scores_int)):
        if scores_int[i] < 35:
            not_pass.append(names[i])
    if not not_pass:
        return "Все сдали"
    else:
        not_pass.insert(0, "Есть не сдавшие")
        return '\n'.join(not_pass)

scores_input = input()
names_input = input()
result = check_all_students_passed(scores_input, names_input)
print(result)
