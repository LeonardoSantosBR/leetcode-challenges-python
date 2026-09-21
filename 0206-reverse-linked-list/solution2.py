# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        if not head or not head.next: #*recursive*
            return head

        new_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return new_head

solution = Solution()
print(solution.reverseList([1,2,3,4,5])) 
print(solution.reverseList([1,2])) 