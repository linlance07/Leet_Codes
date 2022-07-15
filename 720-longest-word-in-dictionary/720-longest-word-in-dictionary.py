class Node:
    def __init__(self):
        self.children = defaultdict(Node)
        self.eow = False

class Solution:
    def __init__(self):
        self.root = Node()

    def longestWord(self, words: List[str]) -> str:
        for word in words:
            temp = self.root
            for l in word:
                if l not in temp.children:
                    temp.children[l] = Node()
                temp = temp.children[l]
            temp.eow = True
        ans = ""
        temp = self.root
        def find(temp,path):
            nonlocal ans
            print(path,len(temp.children))
            if len(path)==len(ans):
                if path<=ans:
                    ans = path
            elif len(path)>len(ans):
                ans = path
            if not temp.children:
                return
            for i in temp.children:
                if temp.children[i].eow:
                    find(temp.children[i],path+i)  
        find(temp,"")
        return ans