#!/usr/bin/env python
# encoding: utf-8
"""
@author: AC4Fun
@license: huifangshuyuan.com
@contact: ximuzmzj@gmail.com
@file: 53. Maximum Subarray.py
@time: 2022-01-10 08:15
@desc: doc
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.



Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Example 2:

Input: nums = [1]
Output: 1
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23


Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104


Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"""

# 动态规划的思想：记f(i)是以nums[i]结尾的最大子数组的和，则f(i)=max(f(i-1)+nums[i], nums[i])
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        f = 0
        result = nums[0]
        for e in nums:
            f = max(f + e, e)
            result = max(result, f)
        return result

# 还有一种分治算法，先跳过，https://leetcode-cn.com/problems/maximum-subarray/solution/zui-da-zi-xu-he-by-leetcode-solution/



