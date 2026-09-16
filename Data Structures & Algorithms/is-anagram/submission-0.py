class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s = {}
        count_t = {}
        for i in s:
            if i in count_s:
                count_s[i] = count_s[i] + 1
            else:
                count_s[i] = 1

        for j in t:
            if j in count_t:
                count_t[j] = count_t[j] + 1
            else:
                count_t[j] = 1

        if count_s == count_t:
            return True

        else:
            return False

