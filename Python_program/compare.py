import random
import time
import cProfile
from line_profiler import LineProfiler

# 定义排序算法
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# 创建一个 LineProfiler 实例
profiler = LineProfiler()

# 使用装饰器来标记需要分析的函数
@profiler
def profile_insertion_sort():
    arr = [random.randint(0, 1000) for _ in range(1000)]
    insertion_sort(arr.copy())

@profiler
def profile_quick_sort():
    arr = [random.randint(0, 1000) for _ in range(1000)]
    quick_sort(arr.copy())

# 使用 cProfile 进行总体性能分析
def cProfile_analysis():
    print("Starting insertion sort profiling...")
    cProfile.run('profile_insertion_sort()', 'insertion_sort_profile.prof')

    print("Starting quick sort profiling...")
    cProfile.run('profile_quick_sort()', 'quick_sort_profile.prof')

# 主程序
if __name__ == "__main__":
    # 运行 cProfile 分析
    cProfile_analysis()
    
    # 运行 line_profiler 分析
    print("Starting line profiler for insertion sort...")
    profile_insertion_sort()
    print("Line profiler stats for insertion sort:")
    profiler.print_stats()
    
    print("Starting line profiler for quick sort...")
    profile_quick_sort()
    print("Line profiler stats for quick sort:")
    profiler.print_stats()
