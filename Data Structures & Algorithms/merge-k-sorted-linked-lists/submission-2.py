# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None

        def merge(list1, list2):
            dummy = ListNode()
            curr = dummy
            
            while list1 and list2:
                if list1.val < list2.val:
                    curr.next = list1
                    list1 = list1.next
                else:
                    curr.next = list2
                    list2 = list2.next    
                curr = curr.next

            if list1:
                curr.next = list1
            
            if list2:
                curr.next = list2

            return dummy.next

        while len(lists) > 1:
            n = len(lists)
            new_lists = []
            for i in range(0, n, 2):
                if (i + 1) < n:
                    new_lists.append(merge(lists[i], lists[i + 1]))
                else: 
                    new_lists.append(lists[i])
            lists = new_lists
        return lists[0]
