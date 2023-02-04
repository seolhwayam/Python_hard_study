# 함수 (Function)

# 재귀함수
# 함수 안에서 자기자신을 호출하는 함수

# 팩토리얼(!)
# 5! = 5 X 4 X 3 X 2 X 1

def factorial_loop(n):
    """
    팩토리얼 함수 by 반복문 사용
    """
    result = 1
    for i in range(1,n+1):
        result = result * i
    return result

print(factorial_loop(5))

def factorial_recursion(n):
    """
    팩토리얼 by 재귀함수
    f(n) = n * (n-1) * (n-2) * (n-3) * ... *1

    f(n) = n * f(n-1)
    f(3) = 3 * f(2)
         = 3 * 2 * f(1)
         = 3 * 2 * 1 * f(0)[1로 return 받음]
         = 3 * 2 * 1 * 1
    """
    if n == 0:
        return 1
    else:
        return n * factorial_recursion(n-1)

print(factorial_recursion(4))

