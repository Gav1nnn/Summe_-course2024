from memory_profiler import profile

# 插入排序实现
@profile
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# 快速排序实现
@profile
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# 测试函数
def main():
    import random
    size = 1000
    arr = [random.randint(0, 10000) for _ in range(size)]
    
    print("Insertion Sort:")
    insertion_sort(arr.copy())
    
    print("Quick Sort:")
    quick_sort(arr.copy())

if __name__ == "__main__":
    main()
