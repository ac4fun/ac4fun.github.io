#!/usr/bin/env python
# encoding: utf-8
"""
@author: AC4Fun
@license: huifangshuyuan.com
@contact: ximuzmzj@gmail.com
@file: 82. Remove Duplicates from Sorted List II.py
@time: 2022-01-08 22:22
@desc: doc
Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.



Example 1:


Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]
Example 2:


Input: head = [1,1,1,2,3]
Output: [2,3]


Constraints:

The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.
"""

# 2次遍历，先找出要删除的值，然后再删除
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        dummy = ListNode(0, head)

        slow = head
        fast = head.next
        deleted_val = []
        while fast is not None:
            if fast.val == slow.val:
                deleted_val.append(fast.val)
            fast = fast.next
            slow = slow.next

        print("deleted_val", deleted_val)
        p = dummy
        q = p.next
        while q is not None:
            if q.val in deleted_val:
                p.next = q.next
                del q
                q = p.next
            else:
                q = q.next
                p = p.next
        return dummy.next



# 一次遍历

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        dummy = ListNode(0, head)

        p = dummy
        q = p.next
        tmp_val = None
        while q and q.next:
            if q.next.val == q.val or (tmp_val is not None and q.val == tmp_val):
                tmp_val = q.val
                p.next = q.next
                del q
                q = p.next
            else:
                q = q.next
                p = p.next
        if tmp_val is not None and q.val == tmp_val:
            p.next = q.next
            del q
            q = p.next
        result = dummy.next
        del dummy
        return result




