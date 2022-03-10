"""Кодировка по умолчанию в Windows 10"""
import locale


# При запуске на других ОС вывод может отличаться. Например у Max OS X и 
# GNU/Linux предпологается кодировка UTF-8.
print(locale.getpreferredencoding())
# На W10 вывод: cp1252
