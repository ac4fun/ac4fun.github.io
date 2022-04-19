#!/usr/bin/env python
# encoding: utf-8
"""
@author: AC4Fun
@license: huifangshuyuan.com
@contact: ximuzmzj@gmail.com
@file: 844. Backspace String Compare.py
@time: 2022-01-09 16:47
@desc: doc
Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.



Example 1:

Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".
Example 2:

Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".
Example 3:

Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".


Constraints:

1 <= s.length, t.length <= 200
s and t only contain lowercase letters and '#' characters.
"""

# 方法一：遍历两次字符串，得到新的字符串后比较
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def build(s: str) -> str:
            result = list()
            for ch in s:
                if ch != '#':
                    result.append(ch)
                elif result:
                    result.pop()

            return result

        return build(s) == build(t)


# 方法二：双指针法，从后向前遍历，可以原地判断，空间复杂度O(1), 时间复杂度仍然是O(m+n)
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        p1 = len(s) - 1
        p2 = len(t) - 1
        skip1 = 0
        skip2 = 0
        while p1 >= 0 or p2 >= 0:
            while p1 >= 0:
                if s[p1] == '#':
                    skip1 += 1
                    p1 = p1 - 1
                elif skip1 > 0:
                    skip1 = skip1 - 1
                    p1 = p1 - 1
                else:
                    break
            # print("p1,p2,skip1,skip2",p1,p2,skip1,skip2)
            while p2 >= 0:
                if t[p2] == '#':
                    skip2 += 1
                    p2 = p2 - 1
                elif skip2 > 0:
                    skip2 = skip2 - 1
                    p2 = p2 - 1
                else:
                    break
            # print("p2",p2)
            if p1 >= 0 and p2 >= 0:
                if s[p1] != t[p2]:
                    return False
            elif p1 >= 0 or p2 >= 0:
                return False
            p1 = p1 - 1
            p2 = p2 - 1
        return True






