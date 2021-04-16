# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def arr2list(arr):
    dummy = ListNode()
    cur = dummy
    for a in arr:
        cur.next = ListNode(a)
        cur = cur.next
    return dummy.next

def list2arr(_list):
    arr = []
    cur = _list
    while cur:
        arr.append(cur.val)
        cur = cur.next
    return arr
