"""Merge k Sorted Lists"""
"""Link to the problem: https://leetcode.com/problems/merge-k-sorted-lists/"""

# Definition for singly-linked list.
from queue import PriorityQueue


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: list[[ListNode]]) -> [ListNode]:
        dummy = ListNode(0)
        curr = dummy
        pq = PriorityQueue()

        for i, lst in enumerate(lists):
            if lst:
                pq.put((lst.val, i, lst))

        while not pq.empty():
            _, i, minNode = pq.get()
            if minNode.next:
                pq.put((minNode.next.val, i, minNode.next))
            curr.next = minNode
            curr = curr.next

        return dummy.next

    def printList(self, node):
        temp = node
        while temp.next is not None:
            print(temp.val, end=" -> ")
            temp = temp.next
        print(temp.val, end=" ")


if __name__ == '__main__':
    solution = Solution()

    # Number of linked lists
    k = 3

    # an array of pointers storing the head nodes of the linked lists
    arr = [None for i in range(k)]

    arr[0] = ListNode(1)
    arr[0].next = ListNode(3)
    arr[0].next.next = ListNode(5)
    arr[0].next.next.next = ListNode(7)
    print("[")
    solution.printList(arr[0])

    arr[1] = ListNode(2)
    arr[1].next = ListNode(4)
    arr[1].next.next = ListNode(6)
    arr[1].next.next.next = ListNode(8)
    print(",")
    solution.printList(arr[1])

    arr[2] = ListNode(0)
    arr[2].next = ListNode(9)
    arr[2].next.next = ListNode(10)
    arr[2].next.next.next = ListNode(11)
    print(",")
    solution.printList(arr[2])
    print("]")
    # Merge all lists
    head = solution.mergeKLists(arr)

    solution.printList(head)
