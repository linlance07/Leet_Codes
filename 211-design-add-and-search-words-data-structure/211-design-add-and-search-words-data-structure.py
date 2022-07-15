class Node:
    def __init__(self):
        self.children = defaultdict(Node)
        self.eow = False
        
class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        temp = self.root
        for l in word:
            if l not in temp.children:
                temp.children[l] = Node()
            temp = temp.children[l]
        temp.eow = True

    def search(self, word: str) -> bool:
        temp = self.root
        def find(temp,ind):
            if ind==len(word):
                if temp.eow:
                    return True
                return False
            if word[ind]=='.':
                res = 0
                for i in temp.children:
                    res = res or find(temp.children[i],ind+1)
                return res
            else:
                if word[ind] in temp.children:
                    return find(temp.children[word[ind]],ind+1)
                return False
        return find(temp,0)
            
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)