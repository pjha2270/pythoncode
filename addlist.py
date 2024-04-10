class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode()  # Initialize dummy head
        current = dummy_head
        carry = 0

        while l1 or l2 or carry:
            # Calculate the sum of current nodes' values and carry
            total_sum = carry
            if l1:
                total_sum += l1.val
                l1 = l1.next
            if l2:
                total_sum += l2.val
                l2 = l2.next

            # Update carry and create a new node for the result
            carry, digit = divmod(total_sum, 10)
            current.next = ListNode(digit)
            current = current.next

        return dummy_head.next  # Return the actual result

# Example usage:
# l1 = ListNode(2, ListNode(4, ListNode(3)))
# l2 = ListNode(5, ListNode(6, ListNode(4)))
# solution = Solution()
# result = solution.addTwoNumbers(l1, l2)
# print(result)  # Output: [7, 0, 8]
