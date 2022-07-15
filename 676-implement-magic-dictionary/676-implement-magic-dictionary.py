class Node:
    def __init__(self):
        self.children = defaultdict(Node)
        self.eow = False

class MagicDictionary:

    def __init__(self):
        self.root = Node()

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            temp = self.root
            for l in word:
                if l not in temp.children:
                    temp.children[l] = Node()
                temp = temp.children[l]
            temp.eow = True

    def search(self, searchWord: str) -> bool:
        temp = self.root
        #print(searchWord)
        def find(temp,ind,act):
            if ind==len(searchWord):
                if temp.eow and act:
                    return True
                return False
            res = 0
            for i in temp.children:
                if i==searchWord[ind]:
                    res |= find(temp.children[searchWord[ind]],ind+1,act)
                if i!=searchWord[ind]:
                    if not act:
                        res |= find(temp.children[i],ind+1,not act)
            return res
        return find(temp,0,0)
        


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)