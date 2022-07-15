class Node:
    def __init__(self):
        self.children = defaultdict(Node)
        self.eow = False

class Trie:

    def __init__(self):
        self.root = Node()
        

    def insert(self, word: str) -> None:
        temp = self.root
        for l in word:
            if l not in temp.children:
                temp.children[l] = Node()
            temp = temp.children[l]
        temp.eow = True
            

    def search(self, word: str) -> bool:
        temp = self.root
        for l in word:
            if l not in temp.children:
                return False
            temp = temp.children[l]
        if temp.eow:
            return True
        return False
        
    def startsWith(self, prefix: str) -> bool:
        temp = self.root
        for l in prefix:
            if l not in temp.children:
                return False
            temp = temp.children[l]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)