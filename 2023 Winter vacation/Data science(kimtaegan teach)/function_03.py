def fibo_recursion(n):
    """
    f(1) = 1
    f(2) = 1
    f(n) = f(n-1) + f(n-2)
    f(3) = f(2) + f(1)
         =  1 + 1

    f(4) = f(3) + f(2)

    :param n:
    :return:
    """
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return fibo_recursion(n-1) + fibo_recursion(n-2)

for k in range(1,8):
    print('피보나지 {0} : {1}'.format(k,fibo_recursion(k)))


# 함수의 매개변수로 함수 전달하기


def print_hi(hi):
    for k in range(5):
        hi()

def hi():
    print('Hello~')

hi()
print_hi(hi)