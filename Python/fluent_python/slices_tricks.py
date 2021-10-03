"""
    silce - это срезы в питон вида s[a:b:c] (a - start, b - stop, c - step)
"""

table_text = """
Jhon    Carter    Male    40
Mari    Ave       Female  38
Clint   Eastwood  Male    62
"""
NAME = slice(0, 7)
SURNAME = slice(8, 17)
SEX = slice(18, 25)
AGE = slice(26, None)

line_items = table_text.split('\n')[1:]
for item in line_items:
    print(item[NAME].strip(), item[AGE].strip(), item[SEX].strip())

# Jhon 40 Male
# Mari 38 Female
# Clint 62 Male

l = list(range(10))
l[2:5] = [20, 30]   # [0, 1, 20, 30, 5, 6, 7, 8, 9]
del l[5:7]          # [0, 1, 20, 30, 5, 8, 9]
l[3::2] = [11, 22]  # [0, 1, 2, 11, 5, 22, 9]
