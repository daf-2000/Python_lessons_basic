# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

a = input('Введите координаты первой точки через пробел \'X Y\': ').split()
b = input('Введите координаты второй точки через пробел \'X Y\': ').split()
c = input('Введите координаты третей точки через пробел \'X Y\': ').split()
class treangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def line_len(a,b):
       len = ((int(a[0]) - int(b[0]))**2 + (int(a[1]) - int(b[1]))**2)**0.5
       return len
    _ab = line_len(a,b)
    _ac = line_len(a,c)
    _bc = line_len(b,c)
    def per(self):
        per1 = self._ac + self._ab + self._bc
        return print('Периметр треугольника: {}'.format(per1))
    def tr_area(self):
        p = (self._ab + self._ac + self._bc) / 2
        S = (p * (p - self._ac) * (p - self._ab) * (p - self._bc))**0.5
        return print('Площадь треугольника: {}'.format(S))
    def check(self):
        if ((int(self.c[0]) - int(self.a[0])) / (int(self.b[0]) - int(self.a[0])) == (int(self.c[1]) - int(self.a[1])) / (int(self.b[1]) - int(self.a[1]))):
            return print('Все точки на одной прямой')
        else:
            return print('Ok')
    def heights(self):
        p = (self._ab + self._ac + self._bc) / 2
        h_ac = 2 * ((p * (p - self._ac) * (p - self._ab) * (p - self._bc)) ** 0.5)/self._ac
        h_ab = 2 * ((p * (p - self._ac) * (p - self._ab) * (p - self._bc)) ** 0.5) / self._ab
        h_bc = 2 * ((p * (p - self._ac) * (p - self._ab) * (p - self._bc)) ** 0.5) / self._bc
        return print('Высоты треугольника равны: H1: {},  H2: {}, H3: {}'.format(h_ac,h_ab,h_bc))


tr1 = treangle(a,b,c)
tr1.tr_area()
tr1.per()
tr1.heights()

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

