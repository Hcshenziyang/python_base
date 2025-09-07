"""
给定一个表示大整数的整数数组digits，其中digits[i]是整数的第i位数字。
这些数字按从左到右，从最高位到最低位排列。这个大整数不包含任何前导0。将大整数加 1，并返回结果的数字数组。
"""


class Solution1:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = length = len(digits)-1
        while digits[i] == 9:
            i -= 1
            if i == -1:
                return [1]+[0]*(length+1)
        digits[i] += 1
        digits[i+1:length+1] = [0]*(length - i)
        return digits

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1] + digits