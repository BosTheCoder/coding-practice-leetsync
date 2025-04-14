from dataclasses import dataclass

@dataclass
class Node:
    key: int
    val: int = 0
    next: Optional['Node'] = None
    prev: Optional['Node'] = None
    
class LRUCache:

    def __init__(self, capacity: int):
        self.head = Node(key=-1)
        self.tail = Node(key=-2)
        self.head.next, self.tail.prev = self.tail,self.head
        self.hash = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.hash:
            value = self.hash[key].val
            # update the position of the node that's accessed
            # it should be popped and added to the tail
            # pop node
            temp = self.hash[key]
            temp.prev.next, temp.next.prev = temp.next, temp.prev

            # add to tail
            prev = self.tail.prev
            prev.next, temp.prev = temp, prev
            temp.next,self.tail.prev = self.tail, temp

            return value
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.hash:
            self.hash[key].val = value
            # you should also update the node here

            # it should be popped and added to the tail
            # pop node
            temp = self.hash[key]
            temp.prev.next, temp.next.prev = temp.next, temp.prev

            # add to tail
            prev = self.tail.prev
            prev.next, temp.prev = temp, prev
            temp.next,self.tail.prev = self.tail, temp

            return
        # create new node
        temp = Node(key=key,val=value)

        # add it to hash
        self.hash[key] = temp
        
        # add node to tail
        prev = self.tail.prev
        prev.next, temp.prev = temp, prev
        temp.next,self.tail.prev = self.tail, temp


        # check if hash now exceeds capacity
        if len(self.hash) > self.capacity:

            # if it does delete the node from thehead and remove it from the hash
            head_node = self.head.next
            del self.hash[head_node.key]
            head_plus_2 = self.head.next.next
            self.head.next, head_plus_2.prev = head_plus_2, self.head





# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)