# Задача:
# Створіть дві змінні first=10, second=30.
# Виведіть на екран результат математичної взаємодії (+, -, *, / и тд.) для цих чисел.
first = 10
second = 30
print(
    first + second,
    first - second,
    first * second,
    first / second,
    first ** second,
    first % second,
    first // second,
    sep="\n")

# Задача:
# Створіть змінну и по черзі запишіть в неї результат порівняння (<, > , ==, !=) чисел з завдання 1.
# Виведіть на екран результат кожного порівняння.

result = first < second
print(result)

result = first > second
print(result)

result = first == second
print(result)

result = first != second
print(result)

# Задача:
# Створіть змінну - результат конкатенації (складання) строк str1="Hello " і str2="world". Виведіть на екран.
first_word = 'Hello '
second_word = 'world'
answer = first_word + second_word
print(answer)
