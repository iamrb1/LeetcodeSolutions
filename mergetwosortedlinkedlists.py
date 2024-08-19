class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1, list2):
    if list1 is None:
        if list2 is None:
            return None
        else:
            return list2
    else:
        if list2 is None:
            return list1

    arr = []
    while list1 is not None:
        arr.append(list1.val)
        list1 = list1.next
    while list2 is not None:
        arr.append(list2.val)
        list2 = list2.next
    arr.sort()

    curr = dummy = ListNode(0)
    for ele in arr:
        curr.next = ListNode(ele)
        curr = curr.next
    return dummy.next

if __name__ == '__main__':
    list1 = ListNode(1,ListNode(2,ListNode(4,None)))
    list2 = ListNode(1,ListNode(3,ListNode(5,None)))
    print(mergeTwoLists(list1,list2))