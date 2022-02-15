def fib_recursive(n: int) -> int:


    if n == 0:
        return 0
    if n == 1:
        return 1

    return fib_iterative(n - 1) + fib_iterative(n - 2)





def fib_iterative(n: int) -> int:
    """
    Calculate n-th number of Fibonacci sequence using iterative algorithm

    n>=0

    :param n: number of item
    :return: Fibonacci number
    """
    if n == 0: # это первое число фиббоначи
        return 0
    if n == 1:
        return 1

    a = 0
    b = 1
    for _ in range(n - 1):
        # sum_ = a + b
        # a = b
        # b = sum_
        a, b = b, a+b

    return b


def generator_fib(n: int) -> int:
    """

    Возвращает первые n чисел фиббоначи
    :return:
    """

    a = 0
    yield a

    b = 1
    yield b

    for _ in range(n - 1):
        a, b = b, a+b
        yield b

N = 10
list_fib_iterative = [fib_iterative(i) for i in range(N)]   #O(n^2)
list_generator_fib = [num for num in generator_fib(9)]   # O(n)


# if __name__ == '__main__':
#     print(fib_iterative(9))
#     print(list(generator_fib(9)))
#     print("---------------------------------")
#     print(list_fib_iterative)
#     print(list_generator_fib)
#     print("---------------------------------")
#     print(fib_recursive(9))