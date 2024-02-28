# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        check = set(nums)
        ans = 0
        dummy = head
        found = False
        while dummy:
            if dummy.val in check:
                found = True
            else:
                if found:
                    ans += 1
                found = False
            dummy = dummy.next
        if found:
            ans += 1
        return ans