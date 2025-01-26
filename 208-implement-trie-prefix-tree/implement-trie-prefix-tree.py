from dataclasses import dataclass

@dataclass
class Node:
    val: str
    children: list["Node"]
    
END_NODE = Node("END_NODE",[])
class Trie:

    def __init__(self):
        self.root = Node("",[])

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            

            matching_nodes = [node for node in curr.children if node.val == c]
            if len(matching_nodes) == 1:
                curr = matching_nodes[0]
            else:
                child = Node(c,[])
                curr.children.append(child)
                curr = child
        curr.children.append(END_NODE)

    def search(self, word: str) -> bool:
        # print()
        # print("SEARCHING\n",self.root)
        curr = self.root
        for c in word:
            matching_nodes = [node for node in curr.children if node.val == c]
            if len(matching_nodes) == 1:
                node = matching_nodes[0]
                curr = node
            else:
                return False
        if len([node for node in curr.children if node == END_NODE]) > 0:
            return True
        return False


    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            matching_nodes = [node for node in curr.children if node.val == c]
            if len(matching_nodes) == 1:
                node = matching_nodes[0]
                curr = node
            else:
                return False
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)