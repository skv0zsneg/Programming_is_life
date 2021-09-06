"""
    Для запуска пайтон скрипта прямо из shell и получения резутата там же:
"""
# root@root> python -c "print('Hi')"
# Hi
# root@root>

"""
    Для запуска пайтон скрипта прямо из shell и получения резутата в файл (поток stdout направлен в файл):
"""
# root@root> python -c "print('Hi')" >> file.txt
# root@root> cat file.txt
# Hi
# root@root>