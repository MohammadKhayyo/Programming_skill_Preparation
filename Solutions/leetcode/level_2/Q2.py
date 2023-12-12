"""Longest Substring Without Repeating Characters"""
import collections

"""Link to the problem: https://leetcode.com/problems/longest-substring-without-repeating-characters/"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        count = collections.Counter()

        l = 0
        for r, c in enumerate(s):
            count[c] += 1
            while count[c] > 1:
                count[s[l]] -= 1
                l += 1
            ans = max(ans, r - l + 1)

        return ans


if __name__ == '__main__':
    solution = Solution()
    Input = "abcabcbb"
    Output = solution.lengthOfLongestSubstring(Input)  # Expected Output: 3
    print(Output)

    Input = "bbbbb"
    Output = solution.lengthOfLongestSubstring(Input)  # Expected Output: 1
    print(Output)

    Input = "pwwkew"
    Output = solution.lengthOfLongestSubstring(Input)  # Expected Output: 3
    print(Output)
