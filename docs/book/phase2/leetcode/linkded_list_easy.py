# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        while head.next:
            if head.val == head.next.val:
                head.next = head.next.next
            else:
                head = head.next
        return head

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, quick = head, head
        while quick and quick.next:
            slow = slow.next
            quick = quick.next.next
            if slow == quick:
                return True
        return False

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head
        seen = set()
        while curr:
            if curr in seen:
                return True
            seen.add(curr)
            curr = curr.next
        return False

class Solution:
    """
    160. Intersection of Two Linked Lists
    """
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        curr_a, curr_b = headA, headB
        while curr_a != curr_b:
            curr_a = curr_a.next if curr_a else headB
            curr_b = curr_b.next if curr_b else headA
        return curr_a

class Solution:
    """
    203. Remove Linked List Elements
    """
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0, head) # add a dummy head
        prev, curr = dummy, head
        while curr:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        return dummy.next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dumpy_head =ListNode(0,None)
        current = head
        while current:
            next_node = current.next
            current.next = dumpy_head.next
            dumpy_head.next = current
            current = next_node
        return dumpy_head.next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        """use idea from reverse linked list"""
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        prev, curr = None, slow
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True


class ListNode:
    def __init__(self, val=-1, next=None):
        self.val = val
        self.next = next

class MyHashSet:
    def __init__(self):
        self.size = 1009  # Prime number for better hash distribution
        self.buckets = [ListNode() for _ in range(self.size)]

    def _hash(self, key: int) -> int:
        return key % self.size

    def add(self, key: int) -> None:
        h = self._hash(key)
        curr = self.buckets[h]
        while curr.next:
            if curr.next.val == key:
                return  # Key already exists
            curr = curr.next
        curr.next = ListNode(key)

    def remove(self, key: int) -> None:
        h = self._hash(key)
        curr = self.buckets[h]
        while curr.next:
            if curr.next.val == key:
                curr.next = curr.next.next
                return
            curr = curr.next

    def contains(self, key: int) -> bool:
        h = self._hash(key)
        curr = self.buckets[h].next
        while curr:
            if curr.val == key:
                return True
            curr = curr.next
        return False

class ListNode:
    def __init__(self, key=-1, value=-1, next=None):
        self.key = key
        self.value = value
        self.next = next

class MyHashMap:
    def __init__(self):
        self.size = 1009
        self.buckets = [ListNode() for _ in range(self.size)]

    def _hash(self, key: int) -> int:
        return key % self.size

    def put(self, key: int, value: int) -> None:
        h = self._hash(key)
        curr = self.buckets[h]
        while curr.next:
            if curr.next.key == key:
                curr.next.value = value
                return
            curr = curr.next
        curr.next = ListNode(key, value)

    def get(self, key: int) -> int:
        h = self._hash(key)
        curr = self.buckets[h].next
        while curr:
            if curr.key == key:
                return curr.value
            curr = curr.next
        return -1

    def remove(self, key: int) -> None:
        h = self._hash(key)
        curr = self.buckets[h]
        while curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
                return
            curr = curr.next

