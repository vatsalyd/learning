class Solution:
    def deleteDuplicates(self, head):
        current = head

        while current and current.next:
            if current.val == current.next.val:
                # Remove the duplicate node
                current.next = current.next.next
            else:
                # Move to the next node
                current = current.next

        return head