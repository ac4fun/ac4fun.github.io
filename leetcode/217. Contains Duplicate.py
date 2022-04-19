#!/usr/bin/env python
# encoding: utf-8
"""
@author: AC4Fun
@license: huifangshuyuan.com
@contact: ximuzmzj@gmail.com
@file: 217. Contains Duplicate.py
@time: 2022-01-10 08:01
@desc: doc
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.



Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true


Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
"""

# 先快排，然后遍历一次判断。或者用hash表
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_hash = {}
        for e in nums:
            if e in nums_hash:
                return True
            else:
                nums_hash[e] = 1
        return False

