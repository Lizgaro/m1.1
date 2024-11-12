# Количество выполненных ДЗ
number_of_homeworks = 12

# Количество затраченных часов
hours_spent = 1.5

# Название курса
course_name = 'Python'

# Время на одно задание (вычисляется как количество часов, деленное на количество задач)
time_per_homework = hours_spent / number_of_homeworks

# Выводим информацию
print(f"Курс: {course_name}, всего задач: {number_of_homeworks}, затрачено часов: {hours_spent}, среднее время выполнения {time_per_homework} часа.")
