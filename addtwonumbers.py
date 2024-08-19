class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def addTwoNumbers(l1, l2):
    first = []
    while l1 is not None:
        first.append(l1.val)
        l1 = l1.next

    second = []
    while l2 is not None:
        second.append(l2.val)
        l2 = l2.next

    first = first[::-1]
    second = second[::-1]

    first = [str(i) for i in first]
    second = [str(i) for i in second]

    x = int("".join(first))
    y = int("".join(second))
    z = x + y
    z = str(z)
    z_list = []
    for ch in z:
        z_list.append(int(ch))
    z_list = z_list[::-1]

    curr = dummy = ListNode(0)
    for ele in z_list:
        curr.next = ListNode(int(ele))
        curr = curr.next
    return dummy.next

if __name__ == '__main__':
    list1 = ListNode(2, ListNode(4, ListNode(3, None)))
    list2 = ListNode(5, ListNode(6, ListNode(4, None)))
    addTwoNumbers(list1,list2)