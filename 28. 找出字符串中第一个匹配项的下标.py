
class Solution:
    def strStr(self, haystack, needle):
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                for j in range(len(needle)):
                    if i+j>=len(haystack):
                        j = 0
                        break
                    if haystack[i+j] != needle[j]:
                        j = 0
                        break
                if j == len(needle)-1:
                    return i
        return -1

class Solution2:
    def strStr(self, haystack, needle):
        m, n = len(haystack), len(needle)
        for i in range(m - n + 1):  # 保证不会越界
            if haystack[i:i+n] == needle:
                return i
        return -1


class Solution3:
    def strStr(self, haystack, needle):
        if not needle:
            return 0
        n, m = len(haystack), len(needle)

        # 构建 next 数组（最长公共前后缀长度）
        next_arr = [0] * m
        j = 0  # 当前匹配的前缀长度
        for i in range(1, m):
            while j > 0 and needle[i] != needle[j]:
                j = next_arr[j - 1]
            if needle[i] == needle[j]:
                j += 1
            next_arr[i] = j

        # KMP 匹配
        j = 0  # needle 的指针
        for i in range(n):
            while j > 0 and haystack[i] != needle[j]:
                j = next_arr[j - 1]  # 利用 next 数组跳过已匹配部分
            if haystack[i] == needle[j]:
                j += 1
            if j == m:  # 完全匹配
                return i - m + 1
        return -1

test1 = Solution3()
print(test1.strStr("sadbutsad", "sad"))
print(test1.strStr("leetcode", "leeto"))
print(test1.strStr("hello", "sababc"))
print(test1.strStr("aaaaaaaabaaa", "aabaaa"))
print(test1.strStr("abababababababc", "ababaca"))  # [0,0,1,2,3,0,1]