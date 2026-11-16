# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0
        
        # Loop while there are nodes left in l1, l2, or if we still have a carry-over
        while l1 is not None or l2 is not None or carry != 0:
            # Get the value from current nodes, or 0 if the list has ended
            val1 = l1.val if l1 is not None else 0
            val2 = l2.val if l2 is not None else 0
            
            # Add them up along with any carry from the previous step
            total_sum = val1 + val2 + carry
            
            # Calculate the new carry (0 or 1) and the digit to store
            carry = total_sum // 10
            digit = total_sum % 10
            
            # Create a new node with the digit and attach it to our result list
            current.next = ListNode(digit)
            
            # Move our pointers forward
            current = current.next
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
                
        return dummy_head.next
