class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def insertionSortList(head):
    ret = []
    while head is not None:
        if not ret:
            ret.append(head.val)
        else:
            if head.val >= ret[-1]:
                ret.append(head.val)
            else:
                i = len(ret)
                while head.val < ret[i - 1] and i != 0:
                    i -= 1
                ret.insert(i, head.val)
        head = head.next

    cur = dummy = ListNode(0)
    for ele in ret:
        cur.next = ListNode(ele)
        cur = cur.next
    return dummy.next

if __name__ == '__main__':

    head = ListNode(-1,ListNode(5,ListNode(3,ListNode(4,ListNode(0,None)))))
    print(insertionSortList(head))