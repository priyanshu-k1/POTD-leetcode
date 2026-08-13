
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp1 = list1
        temp2 = list2
        dummy = ListNode()
        output = dummy

        while(temp1 and temp2):
            if temp1.val < temp2.val:
                output.next = ListNode(temp1.val)
                temp1 = temp1.next
            else:
                output.next = ListNode(temp2.val)
                temp2 = temp2.next
            output = output.next
        while(temp1):
            output.next = ListNode( temp1.val)
            output = output.next
            temp1 = temp1.next
        while(temp2):
                output.next = ListNode(temp2.val)
                output = output.next
                temp2 = temp2.next

        return dummy.next
        