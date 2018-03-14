# Шаг 5 - Приводим к нижнему регистру и разрезаем
# Объединим шаги 3 и 4.
#
# Импортируйте модуль re
# Прочитайте строку
# Приведите строку к нижнему регистру
# Разрежьте строку с помощью re.split('[^a-z]', string)
# Выведите на печать получившийся список
# Sample Input 1:
#
# Cat's power!
# Sample Output 1:
#
# ['cat', 's', 'power', '']
# Sample Input 2:
#
# Any large snake that "constricts" its prey (see Constriction).
# Sample Output 2:
#
# ['any', 'large', 'snake', 'that', '', 'constricts', '', 'its', 'prey', '', 'see', 'constriction', '', '']
# Sample Input 3:
#
# From 1892 through 1903, the Anaconda mine was the largest copper-producing mine in the world.
# Sample Output 3:
#
# ['from', '', '', '', '', '', 'through', '', '', '', '', '', '', 'the', 'anaconda', 'mine', 'was', 'the', 'largest', 'copper', 'producing', 'mine', 'in', 'the', 'world', '']

import re
S = input().lower()
print(re.split('[^a-z]', S))