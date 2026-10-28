class Node(): 
    def __init__(self, key: int = 0, val: int = 0, prev: Optional['Node'] = None, next: Optional['Node'] = None): 
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.hash_map = {}

        self.most_recent = Node()
        self.least_recent = Node()
        
        self.most_recent.next = self.least_recent
        self.least_recent.prev = self.most_recent


    def get(self, key: int) -> int:
        if key not in self.hash_map:
            return -1

        # move from current position to most most_recent
        target_prev, target_next = self.hash_map[key].prev, self.hash_map[key].next
        target_prev.next = target_next
        target_next.prev = target_prev

        last_most_recent = self.most_recent.next

        self.most_recent.next = self.hash_map[key]
        self.hash_map[key].next = last_most_recent

        self.hash_map[key].prev = self.most_recent
        last_most_recent.prev = self.hash_map[key]

        return self.hash_map[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.hash_map: # exist 
            # update 
            self.hash_map[key].val = value
            # move from current position to most most_recent
            target_prev, target_next = self.hash_map[key].prev, self.hash_map[key].next

            target_prev.next = target_next
            target_next.prev = target_prev

            last_most_recent = self.most_recent.next

            self.most_recent.next = self.hash_map[key]
            self.hash_map[key].next = last_most_recent

            self.hash_map[key].prev = self.most_recent
            last_most_recent.prev = self.hash_map[key]
        else: # create new node and inser to most_recent
            new_node = Node(key, value)
            self.hash_map[key] = new_node
            last_most_recent = self.most_recent.next

            self.most_recent.next = self.hash_map[key]
            self.hash_map[key].next = last_most_recent

            self.hash_map[key].prev = self.most_recent
            last_most_recent.prev = self.hash_map[key]


        # check the length > cap and remove if too long
        if len(self.hash_map) > self.cap: 
            last_least_recent = self.least_recent.prev
            
            last_least_recent.prev.next = self.least_recent
            self.least_recent.prev = last_least_recent.prev

            self.hash_map.pop(last_least_recent.key)
            

        