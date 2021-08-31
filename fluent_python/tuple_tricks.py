first, *center, last = range(11)

print(f"{first}, {center}, {last}")  # 0, [1, 2, 3, 4, 5, 6, 7, 8, 9], 10

"""
    ...
"""

metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]

print('{:15} | {:^9} | {:^9}'.format('', 'lat.', 'long.'))
fmt = '{:15} | {:9.4f} | {:9.4f}'
for name, cc, pop, (latitude, longitude) in metro_areas:
    if longitude <= 0:
        print(fmt.format(name, latitude, longitude))

#                 |   lat.    |   long.  
# Mexico City     |   19.4333 |  -99.1333
# New York-Newark |   40.8086 |  -74.0204
# Sao Paulo       |  -23.5478 |  -46.6358



t = (1, 2, [30, 40])
t[2] = [50, 60]  # Здесь будет ошибка, однако t изменится и примет вид (1, 2, [30, 40, 50, 60])
# Почему так???