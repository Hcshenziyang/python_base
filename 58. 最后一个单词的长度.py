"""
给你一个字符串s，由若干单词组成，单词前后用一些空格字符隔开。
返回字符串中最后一个单词的长度。单词是指仅由字母组成、不包含任何空格字符的最大子字符串。

思考：
唔，如果能够倒着找，找到非空格以及遇到下一个空格之间的字符数。如果正着找的话，那就可以记录一个数字列表，然后把最后一个数字拉出来，
或者设置一个变量，记录下这个数字然后不断更新最后输出。这样来看只用循环一遍即可。似乎没有更好的解法了……
"""


class Solution1:
    def lengthOfLastWord(self, s: str) -> int:
        k = 0
        num = 0
        for i in range(0, len(s)):
            if s[i] != " ":
                k = k + 1

            if k != 0 and s[i] == " ":
                num = k
                k = 0

            if k != 0 and i + 1 == len(s):
                num = k
        return num


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1
        # 先把末尾的空格跳过去
        while i >= 0 and s[i] == " ":
            i -= 1
        # 开始计数
        length = 0
        while i >= 0 and s[i] != " ":
            length += 1
            i -= 1
        return length

