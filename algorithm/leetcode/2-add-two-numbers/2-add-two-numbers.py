# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        len1, len2 = self.getNodeLength(l1), self.getNodeLength(l2)
        head = l1 if len1>=len2 else l2
        n1 = head
        n2 = l2 if n1 == l1 else l1
        has_up = 0
        while n1:
            val = n1.val + (n2.val if n2 else 0) 
            n1.val = val %10 
            has_up = 1 if val > 9 else 0
            if has_up:
                if n1.next:
                    n1.next.val+=1
                else:
                    n1.next = ListNode(1, None)
            n1 = n1.next
            if n2:
                n2 = n2.next
        return head
    
        
    def getNodeLength(self, node: ListNode):
        if not node:
            return 0
        return self.getNodeLength(node.next)+1