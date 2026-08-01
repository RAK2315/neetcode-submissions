class Node:
    def __init__(self,key,val):
        self.key = key
        self.val = val

        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.left = Node(0,0)
        self.right = Node(0,0)

        self.left.next = self.right
        self.right.prev = self.left


    def remove(self,node):
        previos = node.prev
        nxt = node.next

        previos.next = nxt
        nxt.prev = previos


    def add(self,node):
        previos = self.right.prev # right pointers previos node
        nxt = self.right          # right pointer ie current

        # connect previos and currnt
        previos.next = node
        node.prev = previos

        # connect currnet and next
        node.next = nxt
        nxt.prev = node



    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.add(self.cache[key])
            return self.cache[key].val
        return -1

        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])

        self.cache[key] = Node(key,value)
        self.add(self.cache[key])

        if len(self.cache) > self.capacity:
            lr = self.left.next
            self.remove(lr)
            del self.cache[lr.key]


        