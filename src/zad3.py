# Преподаватель отправил студентам ведомости с оценками за экзамен. Определите, кто из студентов набрал проходной балл: 35 баллов или больше. Максимальный балл за экзамен — 55 баллов. Если никто не набрал проходной балл, верните «Никто»‎.‎
# Формат ввода
# Две строки. Первая строка — целые числа, означающие баллы учеников (0 ≤ x ≤ 55), они разделены запятой. Вторая строка — имена учеников, также разделенные через запятую. Гарантируется, что количество оценок и имён в двух строках совпадают.
# Формат вывода
# Имена тех учеников, которые набрали проходной балл на экзамене, в их изначальном порядке. Каждое имя должно начинаться с новой строки, в выводе не должно быть запятых. Строка «Никто», если никто не набрал проходной балл.
from symbol import return_stmt


def filter_passed_students(score_string, name_string):
    """Ваш код"""
    score_string = score_string.split(',')
    score_string = [int(item) for item in score_string]
    name_string = name_string.split(',')
    l = list()
    for i in range(len(score_string)):
        if score_string[i]>35:
            l.append(name_string[i])
    return l

# score_string = input()
score_string = '44,32,10,21,21,51,29,48,23,11,30,48,25,42,44,39,27,26,25'
# name_string = input()
name_string = 'Elena,Ivan,Ivan,Maksim,Elizaveta,Etara,Alina,Ainur,Ruslan,Valentin,Dobrynya,Harry,Yana,Slava,Viktor,Kristina,Julia,Svetlana,Elizaveta'
passed_students = filter_passed_students(score_string, name_string)

if not passed_students:
    print('Пустой')
else:
    for student in passed_students:
        print(student)
