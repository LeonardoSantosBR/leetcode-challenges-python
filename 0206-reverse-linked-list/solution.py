# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        new_list= None #*iterative*
        while head:
           next_node = head.next
           head.next = new_list
           new_list = head
           head = next_node
        return new_list

solution = Solution()
print(solution.reverseList([1,2,3,4,5])) 
print(solution.reverseList([1,2])) 