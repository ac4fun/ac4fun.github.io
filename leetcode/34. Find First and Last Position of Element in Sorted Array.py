#!/usr/bin/env python
# encoding: utf-8
"""
@author: AC4Fun
@license: Baidu Corp. All Rights Reserved.
@contact: ximuzmzj@gmail.com
@file: 34. Find First and Last Position of Element in Sorted Array.py
@time: 2022-01-06 08:26
@desc: doc
"""

"""
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109
"""

# 二分查找变种题目
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = -1
        end = -1
        if len(nums) == 0:
            return [start, end]
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                start = end = mid
                while start >= 0 and nums[start] == target:
                    start = start - 1
                while end <= len(nums) - 1 and nums[end] == target:
                    end = end + 1
                return [start + 1, end - 1]
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return [start, end]


