"""Обработка ошибок, возникающих при использовании кодеков."""


"""Кодирование."""

s = 'йцячю'

print(s.encode('utf-8'))
# b'\xd0\xb9\xd1\x86\xd1\x8f\xd1\x87\xd1\x8e'

# print(s.encode('latin1'))
# UnicodeEncodeError: 'latin-1' codec can't encode characters in position 0-4: 
# ordinal not in range(256)

print(s.encode('latin1', errors='ignore'))
# b''

print(s.encode('latin1', errors='replace'))
# b'?????'

print(s.encode('latin1', errors='xmlcharrefreplace'))
# b'&#1081;&#1094;&#1103;&#1095;&#1102;'


"""Декодирование."""

bs = b'\xd0\xb9\xd1\x86\xd1\x8f\xd1\x87\xd1\x8e'

print(bs.decode('utf-8'))
# йцячю

print(bs.decode('latin1'))  # Вместо ошибки декоидровал то, что не понял.
# Ð¹ÑÑÑÑ

# print(bs.decode('gb2312'))
# UnicodeDecodeError: 'gb2312' codec can't decode byte 0xd1 in position 2: illegal multibyte sequence

print(bs.decode('gb2312', errors='replace'))
# 泄��������