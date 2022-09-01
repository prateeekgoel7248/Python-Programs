class Solution(object):
    def beautySum(self, s):
        from collections import defaultdict
        # d=Counter()
        beauty = 0
        len_s = len(s)
        for start in range(len_s - 1):
            chars_freq = defaultdict(int)
            chars_freq[s[start]] += 1
            for end in range(start + 1, len_s):
                chars_freq[s[end]] += 1
                beauty += max(chars_freq.values()) - min(chars_freq.values())
        return beauty