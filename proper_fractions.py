import math
def proper_fractions(n):
    """Функция определяющая кол-во несократимых дробей под знаменатель N"""
    count = 0
    uncorrect = []      #значения, которые являются делителями знаменателя или имеют общие с ним
    for d in range(2,n): #1 ЭТАП: Нахожедение делителей числа N
        if(n%d == 0):
                uncorrect.append(d)
                count +=1

    chislo = 0
    while (chislo < n-1): #2 ЭТАП: Нахожедение чисел,содержащие делители числа N (например: 6 содержит 3)
        chislo += 1
        for i in uncorrect:
            if(chislo > i and chislo % i == 0):
                uncorrect.append(chislo)
                count+=1
                break
            else:
                continue

    """Вариант подсчёта через 2-а генератора списков:
    1)numbers - все числа,идущие до N
    2)list_counter - чистый список без некорректных значений,определённых ранее"""

    #numbers = [x for x in range(1,n)]
    #list_counter = [element for element in numbers if element not in uncorrect]
    #return len(list_counter)

    """Простой вариант подсчёта кол-ва несократимых дробей"""
    return (n-1-count)

f = proper_fractions(123)
print(f)