# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_data = int(str(self.traverse(l1))[::-1])
        l2_data = int(str(self.traverse(l2))[::-1])
        res = [int(i) for i in str(l1_data+l2_data)[::-1]]
        # print(l1_data, l2_data, res)
        return self.create_ll(res)

    def create_ll(self, data):
        head = None
        curr_ptr = None
        for i in data:
            new_node = ListNode(i)
            if head is None:
                head = new_node
                curr_ptr = head
            else:
                curr_ptr.next = new_node
                curr_ptr = curr_ptr.next
            
        return head

    def traverse(self, l):
        curr_ptr = l
        res = ""

        if curr_ptr.next is None:
            return curr_ptr.val
            
        while curr_ptr is not None:
            res+=str(curr_ptr.val)
            curr_ptr=curr_ptr.next

        return res