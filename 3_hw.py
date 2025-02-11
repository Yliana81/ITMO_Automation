# 2. Функция на вход получает два произвольных числа. Вывести в консоль наибольшее из чисел.

def comparing_numbers(first_num, second_num):
    if first_num>second_num:
        print('Наибольшее число: ' + str(first_num))
    else:
        print('Наибольшее число: ' + str(second_num))

comparing_numbers(105, 230)


#3. Функция на вход получает два произвольных числа. Вывести в консоль “yes”, если они отличаются друг от друга на 135,
# иначе вывести на экран “No”

def numbers_diff(first_num, second_num):
    if abs(first_num-second_num) == 135:
        print('yes')
    else:
        print('No')

numbers_diff(100, 235)


# 4. Функция на вход получает произвольное число от 1 до 12 (номер месяца).
# Вывести название сезона года в консоль (зима, весна, лето, осень)

def season(num):
    if num in [12, 1 , 2]:
        print('зима')
    elif num in range(3, 6):
        print('весна')
    elif num in range(6, 9):
        print('лето')
    else:
        print('осень')

season(12)


#5. Функция на вход получает три произвольных числа. Если все числа больше 10, то вывести на экран “yes”, иначе “no”;

def more_than_ten(num1, num2, num3):
    if num1>10 and num2>10 and num3>10:
        print('yes')
    else:
        print('no')

more_than_ten(30,20,11)



#6. Функция на вход получает список, состоящий из 5 произвольных чисел.
#   Найти количество положительных чисел среди них.

def count_positive_numbers(lst):
    count = 0
    for i in range(0, len(lst)):
        if lst[i]>0:
            count+=1
    return count

print(count_positive_numbers([10, -115, -30, -5, -15]))


# 7. Функция на вход получает 2 переменные.
# a. Кол-во лет (int)
# b. Кол-во месяцев (int)
# Вывести в консоль количество дней за это время. Считать, что в каждом месяце 29 дней.

def number_of_days(year, month):
    days = 29
    print('Количество дней: ' + str(year*(month*days)))

number_of_days(20, 10)





