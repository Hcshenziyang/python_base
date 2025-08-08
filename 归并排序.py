# merge sort 归并排序
# 归并排序
"""
最近在系统的学习数据结构和算法，AI出了个题目：
请从你列出的常见时间复杂度中，选择 O(n)、O(n log n)、O(n^2) 这三种，
并分别举一个 Python 代码片段的例子来对应它们的时间复杂度。
主要是log n这个复杂度我不知道怎么搞出来的（刚开始学习，数据结构和算法一窍不通）
然后AI给了一个归并排序，说这个是O(n log n)的复杂度。
行吧，既然这样，择日不如撞日，现在就学一下归并排序吧。
代码仅供演示逻辑，并非绝对正确。
"""
"""
归并排序分类主要三步：分、治、合/归并。
分就是无限细分，治就是每个模块排序只有一个元素默认就是有序的，合就是合并。
下面是代码运行整个逻辑：
假设1、3、5、2、6、4排序。
1：1、3、5一组，2、6、4一组
2：1一组，3、5一组，2、6、4一组
3：1一组，3一组，5一组，2、6、4一组
4：1单独一组，无需比较。3和5比较（具体比较逻辑见后面介绍），3比5小
5：排序并合并[3,5]
6：排序并合并[1,3,5]
...[2、6、4那组同理，得到[2,4,6]]
7: [1,3,5]和[2,4,6]对比，首先有个左序号和右序号，左序号初始为0，右序号初始也为0
7: 左【0】就是1，右【0】就是2，然后1和2对比，1比2小，那么就是1放入新数组，左序号+1。
7: 左【1】就是3，右【0】就是2，然后3和2对比，3比2大，那么就是2放入新数组，右序号+1。
重复上述循环，直至整个结束。
"""
"""
时间成本计算，假设n是2^n。
n经过多少次分解才能每个数组都是长度为1呢？
n/2^k = 1
k = log2(n)

合并工作每层操作次数是多少呢？
两个指针分别在两个数组上扫描，每次最糟糕也不过是当前层数，复杂度是线性的。

所以最终的结果就是【nlog(n)】

"""

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    return merge(left_sorted, right_sorted)

def merge(left, right):
    merged = []
    left_idx, right_idx = 0, 0  # 左右的指针

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            merged.append(left[left_idx])
            left_idx += 1
        else:
            merged.append(right[right_idx])
            right_idx += 1

    merged.extend(left[left_idx:])
    merged.extend(right[right_idx:])
    return merged

# 假设有个初始数组
a = [1,3,5,2,6,4]

# n = 1000 # 假设n是输入规模
# import random
# large_list = [random.randint(0, n*10) for _ in range(n)]

sorted_list = merge_sort(a)
print(sorted_list)