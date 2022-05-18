string = "/add 31.12 Купить ёлку"


splitted_string = string.split(maxsplit=2)  # по-умолчанию разделителем является пробел
# maxsplit=2 - указывает сколько пробелов считать
print(splitted_string)

date = splitted_string[1]
task = splitted_string[2]

print(date)
print(task)