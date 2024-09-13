from functools import wraps
from collections import defaultdict

# 用于跟踪函数调用次数的字典
call_count = defaultdict(int)

def track_calls(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        call_count[func.__name__] += 1
        return func(*args, **kwargs)
    return wrapper

# 斐波那契数列的函数定义
@track_calls
def fib0():
    return 0

@track_calls
def fib1():
    return 1

s = """@track_calls\ndef fib{}(): return fib{}() + fib{}()"""

# 动态创建斐波那契函数
if __name__ == '__main__':
    for n in range(2, 10):
        exec(s.format(n, n-1, n-2))
    from functools import lru_cache
    for n in range(10):
        exec("fib{} = lru_cache(1)(fib{})".format(n, n))
    # 执行测试
    print(eval("fib9()"))

    # 输出每个函数的调用次数
    print("Function call counts:")
    for func_name, count in call_count.items():
        print(f"{func_name}: {count} times")
