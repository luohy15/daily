# key 1: [0,n)
# key 2: loop invariants
# [l, r) not empty
# [l0, l) < value
# [r, r0) >= value
# https://www.zhihu.com/question/36132386/answer/530313852
def lower_bound(arr, value):
    l = 0
    r = len(arr)
    while l < r:
        mid = (l + r) // 2
        if arr[mid] < value:
            l = mid + 1
        else:
            r = mid
    return l

# loop invariants
# [l, r) not empty
# [l0, l) <= value
# [r, r0) > value
def upper_bound(arr, value):
    l = 0
    r = len(arr)
    while l < r:
        mid = (l + r) // 2
        if arr[mid] <= value:
            l = mid + 1
        else:
            r = mid
    return l