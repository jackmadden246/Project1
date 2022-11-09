
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
import re
string = "Thisisatest"
pattern_1 = '[0-9]'
pattern_2 = '[A-Z]'
pattern_3 = 'Ye$'
pattern_4 = 'T[a-z]*t$'
search_1 = re.search(pattern_1, string)
search_2 = re.search(pattern_2, string)
search_3 = re.search(pattern_3, string)
search_4 = re.search(pattern_4, string)
print(search_1)
print(search_2)
print(search_3)
print(search_4)





