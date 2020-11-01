head =  '1->1->2->3->3'
temp = []
for i in head.split('->'):
    if i not in temp:
        temp.append(i)
print("->".join(temp))



head =  '1->1->2->3->3'
print("->".join(sorted(set(head.split('->')))))


class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if head == None:
            return head

        node = head

        while node.next:
            if node.val == node.next.val:
                node.next = node.next.next
            else:
                node = node.next

        return head
