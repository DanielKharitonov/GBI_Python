# За день машина проезжает n километров. Сколько
# дней нужно, чтобы проехать маршрут длиной m
# киломметров? При решении задачи нельзя пользоваться
# условной инструкцией if и циклами.

n = int(input('Введите сколько километров машина проезжает в день: '))
m = int(input('Введите длину маршрута в километрах: '))
print('Требуемое количество дней: ', -(-m//n))

# При целочисленном делении число округляется в меньшую сторону

