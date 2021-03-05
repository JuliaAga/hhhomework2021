from decorators import cache_decorator
calc = {'+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '/': lambda x, y: x / y if y != 0 else 'division by zero is prohibited',
        '*': lambda x, y: x * y,
        '**': lambda x, y: x ** y,
        }

@cache_decorator
def calculator(a, b, operation):
    # Здесь нужно реализовать функцию,
    # которая реализует основные арифметические операции между числами: +, -, /, *, **.
    # Так же следует сделать проверку, что поступивший оператор корректен (присутствует в этом списке +, -, /, *, **)
    return calc.get(operation)(a, b)


def getIntInput():
    while True:
        try:
            return int(input('Введите число: '))
        except Exception:
            print('Unsupported type of number, try again')

def getOperation():
    while True:
        operation = input('Введите операцию: ')
        if operation in calc:
            return operation
        else:
            print ('Unsupported operation. Supported: + - / * **. Try again')


if __name__ == '__main__':
    while True:
        a = getIntInput() # Тут было бы неплохо обрабатывать ошибку в случае передачи некорректных символов
        b = getIntInput()
        operation = getOperation()

        print('Результат: ', calculator(a, b, operation))

        if input('Остановить? 1 - да, 0 - нет ') == 1:
            exit(0)