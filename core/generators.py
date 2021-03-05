# написать генераторную функцию, которая принимает число N возвращает N рандомных чисел от 1 до 100
import random
def gen(N):
    for i in range(N):
        yield random.uniform(1, 100)

# написать генераторное выражение, которое делает то же самое

if __name__ == '__main__':

    print("Function: ")
    for x in gen(5):
        print(x)

    print("Expression: ")
    for y in (random.uniform(1, 100) for _ in range(5)):
        print(y)
