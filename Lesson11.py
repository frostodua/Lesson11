# 1. Даний текстовий файл. Необхідно створити новий файл, який потрібно
# переписати з першого файлу всі слова, що складаються не менше ніж з семи літер.
#
# 2. Даний текстовий файл. Підрахувати кількість слів у ньому.
#
# 3. Створіть програму, яка перевіряє текст на неприпустимі слова.
#
# Якщо неприпустиме слово знайдено, його слід замінити на набір символів *.
#
# За підсумками роботи програми необхідно показати статистику дій.#
# Наприклад, якщо й у нас є такий текст:
#
# To be, or not to be, that is the question, Whether 'tis nobler in the mind to
# suffer The slings and arrows of outrageous fortune, Or to take arms against a
# sea of troubles, And by opposing end them? To die: to sleep; No more; and by a
# sleep to say we end The heart-ache and the thousand natural shocks That flesh
# is heir to, 'tis a consummation Devoutly to be wish'd. To die, to sleep
#
# Неприпустиме слово: die.
# # Результат:
#
# To be, or not to be, that is the question, Whether 'tis nobler in the mind to
# suffer The slings and arrows of outrageous fortune, Or to take arms against a
# sea of troubles, And by opposing end them? To ***: to sleep; No more; and by a
# sleep to say we end The heart-ache and the thousand natural shocks That flesh is
# heir to, 'tis a consummation Devoutly to be wish'd. To ***, to sleep.
#
# Статистика: 2 заміни слова die.
# # Нотатка:
# # Текст для всіх завдань можна написати самостійно або взяти з Інтернету.
# # Логіка має працювати з будь-яким текстом.

# 1. Даний текстовий файл. Необхідно створити новий файл, який потрібно
# переписати з першого файлу всі слова, що складаються не менше ніж з семи літер.

text = ['''To be, or not to be, that is the question, Whether 'tis nobler in the 
mind to suffer The slings and arrows of outrageous fortune, Or to take arms against 
a sea of troubles, And by opposing end them? To die: to sleep; No more; and by a 
sleep to say we end The heart-ache and the thousand natural shocks That flesh is heir to,
'tis a consummation Devoutly to be wish'd. To die, to sleep''']
text = str(text)

try:
    my_file = open("First_task_Begin.txt", "w")
    try:
        my_file.write(text)
    except Exception as e:
        print(e)
    finally:
        my_file.close()
except Exception as e:
    print(e)

def words_more_6letters(First_task_Begin, First_task_End):
    with open(First_task_Begin, 'r') as file:
        words = file.read().split()

    long_words = [word for word in words if len(word) >= 7]

    with open(First_task_End, 'w') as file:
        file.write(' '.join(long_words))

input_filename = 'First_task_Begin.txt'
output_filename = 'First_task_End.txt'
words_more_6letters(input_filename, output_filename)

# 2. Даний текстовий файл. Підрахувати кількість слів у ньому.

