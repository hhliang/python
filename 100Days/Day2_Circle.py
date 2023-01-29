import math

Radius = float(input('請輸入半徑: '))
Perimeter = 2 * Radius * math.pi
Area = Radius * Radius * math.pi
print ('周長為%.5f' % float(Perimeter))
print ('面積為%.5f' % float(Area))