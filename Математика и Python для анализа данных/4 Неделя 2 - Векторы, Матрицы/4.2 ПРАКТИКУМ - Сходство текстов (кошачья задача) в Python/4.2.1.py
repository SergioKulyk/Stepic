# Шаг 1.1 - открытие файла
# Откройте файл text.txt и выведите его содержимое на печать.
#
# Sample Input:
#
# Text about cats
# Text about Anacondas
# Sample Output:
#
# Text about cats
# Text about Anacondas

with open('text.txt', 'r') as file:
    text = file.readlines()

for line in text:
    print(line.strip())
