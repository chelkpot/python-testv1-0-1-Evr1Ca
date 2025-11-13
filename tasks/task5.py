# tasks/task1.py



def solve():
# Ниже пишите решение задачии(Обязательно поставьте четыре пробела после функции Solve())
    numbers = map(int, input("Введите числа: ").split())
    squares = map(lambda x: x**2, numbers)
    print("Результат:", *squares)
# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()
