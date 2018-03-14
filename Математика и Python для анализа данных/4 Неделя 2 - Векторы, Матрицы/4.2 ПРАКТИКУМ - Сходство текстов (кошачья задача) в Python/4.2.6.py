# Шаг 4 - разрезаем строку с помощью re
# Импортируйте модуль re
# Считайте строку
# Разрежьте её на отдельные слова с помощью re.split('[^a-z]', string)
# Получившийся список выведите на печать
# Sample Input 1:
#
# Cat's power!
# Sample Output 1:
#
# ['', 'at', 's', 'power', '']
# Sample Input 2:
#
# Any large snake that "constricts" its prey (see Constriction).
# Sample Output 2:
#
# ['', 'ny', 'large', 'snake', 'that', '', 'constricts', '', 'its', 'prey', '', 'see', '', 'onstriction', '', '']
# Sample Input 3:
#
# From 1892 through 1903, the Anaconda mine was the largest copper-producing mine in the world.
# Sample Output 3:
#
# ['', 'rom', '', '', '', '', '', 'through', '', '', '', '', '', '', 'the', '', 'naconda', 'mine', 'was', 'the', 'largest', 'copper', 'producing', 'mine', 'in', 'the', 'world', '']

import re
S = input()
print(re.split('[^a-z]', S))
