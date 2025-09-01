"""
移除元素
给你一个数组 nums 和一个值 val，你需要原地移除所有数值等于val的元素。元素的顺序可能发生改变。然后返回 nums 中与 val 不同的元素的数量。
假设 nums 中不等于 val 的元素数量为 k，要通过此题，您需要执行以下操作：
更改 nums 数组，使 nums 的前 k 个元素包含不等于 val 的元素。nums 的其余元素和 nums 的大小并不重要。
返回 k。
提示：
0 <= nums.length <= 100
0 <= nums[i] <= 50
0 <= val <= 100
思考：
删除val值的元素，然后返回其他数值个数。初步来看，就是循环、删除、计数？不过要求原地删除……唔，python里列表用del可以删除，似乎没有什么难的。
emmm……实际发现，直接使用del会导致列表长度变化，然后容易导致循环报错，虽然，虽然也能够约束，但是效果不太稳定。不如直接替换，然后就搞出来了一个双指针法啥的。
"""
class Solution:
    def removeElement(self, nums, val):
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k

class Solution2:
    def removeElement(self, nums, val):
        while val in nums:
            nums.remove(val)
        return len(nums)



test1 = Solution()
print(test1.removeElement([3,2,2,3],3))