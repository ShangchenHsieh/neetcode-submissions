from typing import Optional
class MyHashMap:

    class Node():
        def __init__(self, k: int = -1, v: int = -1, n: Optional['Node'] = None): 
            self.key = k
            self.value = v
            self.next = n

    def __init__(self):
        self.data = [self.Node() for _ in range(1000)]

    def hash(self, key: int):
        return key % len(self.data)

    def put(self, key: int, value: int) -> None:
        entry = self.data[self.hash(key)]
        while entry.next: 
            if entry.next.key == key:
                entry.next.value = value
                return
            entry = entry.next  
        entry.next = self.Node(key, value)

    def get(self, key: int) -> int:
        cur = self.data[self.hash(key)]
        while cur: 
            if cur.key == key:
                return cur.value
            cur = cur.next
        return -1

    def remove(self, key: int) -> None:
        cur = self.data[self.hash(key)]
        while cur.next: 
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)