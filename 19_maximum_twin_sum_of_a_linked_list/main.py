# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def createList(lst):
    prev = ListNode()
    head = prev
    for num in lst:
        prev.next = ListNode(num)
        prev = prev.next
    return head.next


def printList(head):
    print('List: ', end=" ")
    while head is not None:
        print(head.val, end=" ")
        head = head.next
    print()


class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        # lst = []
        # while head is not None:
        #     lst.append(head.val)
        #     head = head.next
        # res = lst[0] + lst[-1]
        # lst = lst[1:-1]
        # while len(lst) > 0:
        #     c = lst[0] + lst[-1]
        #     res = max(res, c)
        #     lst = lst[1:-1]
        # else:
        #     return res
        def split(node):
            l = node
            r = node
            b = None
            while (r is not None and r.next is not None):
                # print(l.val, end="")
                # print(r.val)
                r = r.next.next
                newNode = ListNode(l.val, next=b)
                b = newNode
                l = l.next

            return b, l
        l, r = split(head)
        # printList(l)
        # printList(r)
        res = l.val + r.val
        while l is not None and r is not None:
            res = max(res, l.val+r.val)
            l, r = l.next, r.next
        return res


if __name__ == "__main__":
    head = [5, 4, 2, 1]
    sol = Solution()
    hNode = createList(head)
    # exit()
    # l, r = sol.pairSum(hNode)
    print(sol.pairSum(hNode))
