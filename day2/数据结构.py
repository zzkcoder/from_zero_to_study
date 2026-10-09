'''
三、装饰器实现题：共 30 分
要求：

必须使用 functools.wraps。

必须使用闭包。

必须支持 *args, **kwargs。

写完后解释闭包在哪里。

1. 实现 retry() 装饰器：10 分
要求：

支持参数：times=3、exceptions=(Exception,)、delay=0。

被装饰函数抛出指定异常时，自动重试。

达到最大次数后，最后一次异常继续抛出。

如果 delay > 0，每次重试前等待。

python
@retry(times=3, exceptions=(ValueError,), delay=0.1)
def may_fail():
    ...
2. 实现 timer() 装饰器：10 分
要求：

打印函数名和耗时。

函数有返回值时，必须返回原结果。

函数抛异常时，也要能打印耗时。

python
@timer
def work():
    ...
3. 实现 cache() 装饰器：10 分
要求：

相同参数再次调用时，直接返回缓存结果。

支持位置参数和关键字参数。

关键字参数顺序不同，也应视为同一调用。

如果参数不可哈希，则跳过缓存，直接调用原函数。

python
@cache
def add(a, b):
    ...
'''

#2.
import time
import functools


def timer(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        start_time=time.perf_counter()
        try:
            return func(*args,**kwargs)
        finally:
            end_time=time.perf_counter()
            print(f"{func.__name__}耗时{end_time-start_time:.4f}秒")
        return wrapper