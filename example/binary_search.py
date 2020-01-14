# 二分查找
# 返回 x 在 arr 中的索引，如果不存在返回 -1
def binarySearch (arr, x):
    low = 0  # 最小数下标
    high = len(arr) - 1  # 最大数下标
    while low <= high:
        mid = (low + high) // 2  # 中间数下标
        if arr[mid] == x:  # 如果中间数下标等于val, 返回
            return mid
        elif arr[mid] > x:  # 如果val在中间数左边, 移动high下标
            high = mid - 1
        else:  # 如果val在中间数右边, 移动low下标
            low = mid + 1
    return -1

print(binarySearch(list(range(1, 10)), 3))
