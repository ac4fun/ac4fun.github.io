#!/usr/bin/env python
# encoding: utf-8
"""
@author: AC4Fun
@license: huifangshuyuan.com
@contact: ximuzmzj@gmail.com
@file: 15. 3Sum.py
@time: 2022-01-09 11:08
@desc: doc
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.



Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:

Input: nums = []
Output: []
Example 3:

Input: nums = [0]
Output: []


Constraints:

0 <= nums.length <= 3000
-105 <= nums[i] <= 105
"""


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        result = []
        for i in range(n):
            # 与上一次的循环中的值不同
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            k = n - 1
            target = -nums[i]
            for j in range(i + 1, n):
                # print("i,j,k, result", i, j, k, result)
                # 与上一次的循环中的值不同
                if j > i + 1 and nums[j - 1] == nums[j]:
                    continue
                while k > j and nums[j] + nums[k] > target:
                    k = k - 1
                if j == k:
                    break
                if nums[j] + nums[k] == target:
                    result.append([nums[i], nums[j], nums[k]])
        return result




