import re

class Not_Integer_Exception(Exception):
    def __init__(self, message):
        super().__init__(message)

class Negative_Number_Exception(Exception):
    def __init__(self, message, value):
        message = f'Веденное значение {value} меньше нуля'
        super().__init__(message)

message = "Введено не целое число"

input_list = 123.5

if input_list < 0:
    raise Negative_Number_Exception (message,input_list)
else:
    try:
        square_numbers = int(re.sub('\d', lambda m: str(int(m.group(0)) ** 2), str(input_list)))
        print (f'Квадрат каждой цифры из числа = {square_numbers}')
    except:
        raise Not_Integer_Exception (message)
