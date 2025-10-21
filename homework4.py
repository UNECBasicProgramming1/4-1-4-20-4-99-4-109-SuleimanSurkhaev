import math
Task_Number = int(0)
def Say_Task_Number():
    global Task_Number
    Task_Number += 1
    if Task_Number == 21:
        Task_Number = 99
    print(f'Task №{Task_Number}')

def reset():
    global x, y, k, a, b, r
    x, y = 0, 0
    k, r = 0, 0
    a, b = 0, 0


#1
Say_Task_Number()
reset()

x = int(input('Введите вещественное число №1 ---> '))
y = int(input('Введите вещественное число №2 ---> '))

if x > y:
    print(f"{x} > {y}")
if y > x:
    print(f"{y} > {x}")
if x == y:
    print(f"{x} = {y}")

#2
Say_Task_Number()
reset()

x = int(input('введите x --> '))

if x > 0:
    y = (math.sin(x))**2
    print(f'y = {y}')
if x <= 0:
    y = 1 + 2*math.sin(x**2)
    print(f'y = {y}')

#3
Say_Task_Number()
reset()

x = int(input('введите x --> '))

if x > 0:
    y = math.sin(x**2)
    print(f'y = {y}')
if x <= 0:
    y = 1 + 2*((math.sin(x))**2)
    print(f'y = {y}')

#4
Say_Task_Number()
reset()

x = float(input("введите координату x --> "))
y = float(input("введите координату y --> "))

if x < 4:
    print(f"точка ( {x} {y} ) попадает в область I.")
else:
    print(f"точка ( {x} {y} ) попадает в область II.")

#5
Say_Task_Number()
reset()

x = float(input("введите координату x: "))
y = float(input("введите координату y: "))

if y > 3:
    print(f"точка ( {x} {y} ) попадает в область I.")
else:
    print(f"точка ( {x} {y} ) попадает в область II.")

#6
Say_Task_Number()
reset()

x = float(input("Введите значение x: "))
if x < 2:
    y_a = x
else:
    y_a = 2
if x < 3:
    y_b = -x
else:
    y_b = -3
print(f"Для графика (а): y = {y_a}")
print(f"Для графика (б): y = {y_b}")

#7
Say_Task_Number()
reset()

x = int(input('введите x --> '))
if math.sin(x) < 0:
    k = x**2
    print(f'k = {k}')
if math.sin(x) >= 0:
    k = math.fabs(x)
    print(f'k = {k}')

if x > k:
    f = k*x
    print(f'f = {f}')
if x <= k:
    f = k + x
    print(f'f = {f}')

#8
Say_Task_Number()
reset()

x = int(input('введите x --> '))
if math.sin(x) >= 0:
    k = x**2
    print(f'k = {k}')
if math.sin(x) < 0:
    k = math.fabs(x)
    print(f'k = {k}')

if x >= k:
    f = k*x
    print(f'f = {f}')
if x < k:
    f = math.fabs(x)
    print(f'f = {f}')

#9
Say_Task_Number()
reset()
a = float(input("введите первое число --> "))
b = float(input("введите второе число --> "))

if a != b:
    if a > b:
        max_val, min_val = a, b
    else:
        max_val, min_val = b, a
    print("максимум =", max_val)
    print("минимум =", min_val)
else:
    print("ошибка: числа равны, а они должны быть различны.")

#10
Say_Task_Number()
reset()

km = int(input("веедите растояние в км для сравнения --> "))
feet = int(input("введите растояние в футтах для сравнения --> "))
print(f"если перевести футы в км, то у нас будет {feet * 0.0003048}")
print(f"если перевести км в футы, то у нас будет {km / 0.0003048}")

if (feet * 0.0003048) > km or (km / 0.0003048) < feet:
    print(f"{km} km < {feet} футы")
if (feet * 0.0003048) < km or (km / 0.0003048) > feet:
    print(f"{km} km > {feet} футы")
if (feet * 0.0003048) == km or (km / 0.0003048) == feet:
    print(f"{km} km = {feet} футы")

#11
Say_Task_Number()
reset()

km_hour = int(input("введите скорость км/час для сравнения --> "))
metr_sec = int(input("введите скорость метр/секунду для сравнения --> "))
print(f"если перевести км/час в метры/секунду, то будет {km_hour * 0.278} м/с")
print(f"если перевести метр/секунду в км/час, то будет {metr_sec * 3.6} км/час")

if (metr_sec * 3.6) > km_hour:
    print(f"{km_hour} км/ч < {metr_sec} м/с")
if (metr_sec * 3.6) < km_hour:
    print(f"{km_hour} км/ч > {metr_sec} м/с")
if (metr_sec * 3.6) == km_hour:
    print(f"{km_hour} км/ч = {metr_sec} м/с")

#12
Say_Task_Number()
reset()

r = int(input("радиус круга --> "))
x = int(input("сторона квадрата --> "))
Sb = math.pi * (r**2)
Ss = x**2
if Ss > Sb:
    print(f"площадь круга с радиусом {r} больше площади квадрата со стороной {x}")
if Ss < Sb:
    print(f"площадь круга с радиусом {r} меньше площади квадрата со стороной {x}")
if Ss == Sb:
    print(f"площадь круга с радиусом {r} равна площаде квадрата со стороной {x}")

#13
Say_Task_Number()
reset()

v1 = int(input("введите объем тела №1 --> "))
m1 = int(input("введите массу тела №1 --> "))
v2 = int(input("введите объем тела №2 --> "))
m2 = int(input("введите массу тела №2 --> "))
P1 = m1/v1
P2 = m2/v2
if P1 > P2:
    print(f"плотность тела №1 больше плотности тела №2")
if P1 < P2:
    print(f"плотность тела №1 меньше плотности тела №2")
if P1 == P2:
    print(f"плотность тела №1 равна плотности тела №2")

#14
Say_Task_Number()
reset()

R1 = float(input("введите сопротивление первого участка (Ом): "))
U1 = float(input("введите напряжение на первом участке (В): "))
R2 = float(input("введите сопротивление второго участка (Ом): "))
U2 = float(input("введите напряжение на втором участке (В): "))
I1 = U1 / R1
I2 = U2 / R2
print(f"ток через первый участок: {I1:.4f} А")
print(f"ток через второй участок: {I2:.4f} А")
if I1 < I2:
    print("меньший ток протекает по первому участку.")
elif I2 < I1:
    print("меньший ток протекает по второму участку.")
else:
    print("токи на обоих участках равны.")

#15 и 16
Say_Task_Number()
print("&")
Say_Task_Number()
reset()

a = int(input("введите a (a не должна быть равна 0) --> "))
while a == 0:
    a = int(input("вы ввели a = 0, введите другое a --> "))

b = int(input("введите b --> "))
c = int(input("введите c --> "))
D = b**2 - 4*a*c
if D > 0:
    print("есть 2 корня")
    x1 = ((-b) + math.sqrt(D))/2*a
    x2 = ((-b) - math.sqrt(D))/2*a
    print(f"x1 = {x1:.4f}, x2 = {x2:.4f}")
if D == 0:
    print("есть 1 корень")
    x = (-b)/2*a
if D < 0:
    print("нет корней")

#17
Say_Task_Number()
reset()

print("месяца года по номерам: ")
print("1 - январь, 2 - февраль, 3 - март")
print("4 - апрель, 5 - май, 6 - июнь")
print("7 - июль, 8 - август, 9 - сентябрь")
print("10 - октябрь, 11 - ноябрь, 12 - декабрь")

mouth_b = int(input("введите номер месяца вашего рождения --> "))
while mouth_b < 1 or mouth_b > 12:
    print(f"вы ввели неверное число для месяца. нет месяца под номером {mouth_b}")
    mouth_b = int(input("введите номер месяца вашего рождения --> "))
year_b = int(input("введите год вашего рождения --> "))

mouth_p = int(input("введите номер нынешнего месяца --> "))
while mouth_p < 1 or mouth_p > 12:
    print(f"вы ввели неверное число для месяца. нет месяца под номером {mouth_p}")
    mouth_p = int(input("введите номер нынешнего месяца --> "))
year_p = int(input("введите нынешний год --> "))
year_all = (year_p - year_b)*12
mouth_all = year_all + (mouth_p - mouth_b)
year_all = mouth_all // 12

mouth = ["январь", "февраль", "март", "апрель", "май", "июнь", "июль", "август", "сентябрь", "октябрь", "ноябрь", "декабрь"]
mouth_b = mouth[mouth_b - 1]
mouth_p = mouth[mouth_p - 1]

print(f"возраст человека, рожденого в {mouth_b} {year_b} году, на момент {mouth_p} {year_p} года равен {year_all} лет")

#18
Say_Task_Number()
reset()

circle_area = int(input("введите площадь круга --> "))
square_area = int(input("введите площадь квадрата --> "))

r = math.sqrt(circle_area / math.pi)
a = math.sqrt(square_area)
circle_in_square = 2 * r <= a
square_in_circle = a * math.sqrt(2) <= 2 * r

print(f"круг уместится в квадрате: {circle_in_square}")
print(f"квадрат уместится в круге: {square_in_circle}")

#19
Say_Task_Number()
reset()

circle_area = int(input("введите площадь круга --> "))
triangle_area = int(input("введите площадь треугольника --> "))

r = math.sqrt(circle_area / math.pi)
a = math.sqrt((4 * triangle_area) / math.sqrt(3))
r_in = a / (2 * math.sqrt(3))
r_out = a / math.sqrt(3)
circle_in_triangle = r <= r_in
triangle_in_circle = r >= r_out

print(f"круг уместится в треугольнике: {circle_in_triangle}")
print(f"треугольник уместится в круге: {triangle_in_circle}")

#20
Say_Task_Number()
reset()

print("Введите координаты первого прямоугольника (x1 y1 x2 y2):")
rect1 = list(map(float, input().split()))

print("Введите координаты второго прямоугольника (x1 y1 x2 y2):")
rect2 = list(map(float, input().split()))

bl, tr = rect1, rect2
x1_1, y1_1, x2_1, y2_1 = rect1 
x1_2, y1_2, x2_2, y2_2 = rect2 
min_x = min(x1_1, x1_2)
min_y = min(y1_1, y1_2)
max_x = max(x2_1, x2_2)
max_y = max(y2_1, y2_2)
bottom_left = (min_x, min_y)
top_right = (max_x, max_y)


print(f"Левый нижний угол минимального прямоугольника: {bl}")
print(f"Правый верхний угол минимального прямоугольника: {tr}")

#99 а и б
Say_Task_Number()
reset()

x = int(input("введите число №1 --> "))
y = int(input("введите число №2 --> "))

max = y
if x > y:
    max = x
print(f'наибольшее число это {max}')


#100
Say_Task_Number()
reset()

x = int(input("введите число №1 --> "))
y = int(input("введите число №2 --> "))

max = y
min = y

if x > y:
    max = x
    min = y
print(f'наибольшее число это {max}')
print(f'наименьшее число это {min}')

#101 а и б
Say_Task_Number()
reset()

x = int(input("введите число №1 --> "))
y = int(input("введите число №2 --> "))
z = int(input("введите число №3 --> "))

numbers = [x, y, z]
max = max(numbers)
min = min(numbers)

print(f'наибольшее число это {max}')
print(f'наименьшее число это {min}')

#102 а и б
Say_Task_Number()
reset()

x = int(input("введите число №1 --> "))
y = int(input("введите число №2 --> "))
z = int(input("введите число №3 --> "))
w = int(input("введите число №4 --> "))

numbers = [x, y, z, w]
max = max(numbers)
min = min(numbers)

print(f'наибольшее число это {max}')
print(f'наименьшее число это {min}')

#103
Say_Task_Number()
reset()

x = int(input("введите вещественное число --> "))
if x < 0:
    x = -x
print(f"абсолютное значение = {x}")


#104 а и б
Say_Task_Number()
reset()

x = int(input("введите вещественное число №1 --> "))
y = int(input("введите вещественное число №2 --> "))
z = (x + y)/2
if z < 0:
    z = -z
print(f"абсолютное значение полусуммы = {z}")

z = math.sqrt(x * y)
if z < 0:
    z = -z
print(f"абсолютное значение квадратного корня из произведения заданных чисел= {z}")


#105
Say_Task_Number()
reset()

x = int(input("введите вещественное число №1 --> "))
y = int(input("введите вещественное число №2 --> "))
if math.fabs(x) > math.fabs(y):
    x = x/2
print(f"итог. число 1 = {x} и число 2 = {y}")

#106
Say_Task_Number()
reset()

x = int(input("введите вещественное число №1 --> "))
y = int(input("введите вещественное число №2 --> "))
if x > math.sqrt(y):
    y = y*5
print(f"итог. число 1 = {x} и число 2 = {y}")

#107
Say_Task_Number()
reset()

x = int(input("введите вещественное число №1 --> "))
y = int(input("введите вещественное число №2 --> "))
z = int(input("введите вещественное число №2 --> "))

numbers = [x, y, z]
correct_numbers = [w for w in numbers if w % 2 == 0]
print(f"четные числа: {correct_numbers}")

#108
Say_Task_Number()
reset()

x = int(input("введите вещественное число №1 --> "))
y = int(input("введите вещественное число №2 --> "))
z = int(input("введите вещественное число №2 --> "))

numbers = [x, y, z]
correct_numbers = [w for w in numbers if w < 0]
print(f"отрицательные числа: {correct_numbers}")

#109
Say_Task_Number()
reset()

x = int(input("введите вещественное число №1 --> "))
y = int(input("введите вещественное число №2 --> "))
z = int(input("введите вещественное число №2 --> "))

numbers = [x, y, z]
correct_numbers = [w for w in numbers if w > 1.6 and w < 3.8]
print(f"отрицательные числа: {correct_numbers}")

