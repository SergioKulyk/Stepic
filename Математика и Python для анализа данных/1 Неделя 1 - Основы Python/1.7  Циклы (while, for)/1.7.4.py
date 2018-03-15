# На вход подаётся строка, некоторые слова в которой "испорчены".
#
# Признак "испорченного" слова - 1я буква в нём заменена на *.
#
# Выведете на печать только "не испорченные" слова, каждое с новой строки
#
# Sample Input:
#
# exaggeration *romotion run into admit exactly *idelity *erspective treat check certain
# Sample Output:
#
# exaggeration
# run
# into
# admit
# exactly
# treat
# check
# certain

lst = input().split()
for i in lst:
    if i[0] != '*':
        print(i)
