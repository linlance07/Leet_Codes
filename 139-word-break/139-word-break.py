class Node:
    def __init__(self):
        self.children = defaultdict(Node)
        self.eow = False
        
class Solution:
    def __init__(self):
        self.root = Node()
    
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        for word in wordDict:
            temp = self.root
            for l in word:
                if l not in temp.children:
                    temp.children[l] = Node()
                temp = temp.children[l]
            temp.eow = True
        def search(word):
            temp = self.root
            for l in word:
                if l not in temp.children:
                    return False
                temp = temp.children[l]
            if temp.eow:
                return True
            return False
        dp = [False]*(len(s)+1)
        dp[0] = True
        for i in range(1,len(s)+1):
            for j in range(i):
                if dp[j] and search(s[j:i]):
                    dp[i] = True
                    break
        return dp[-1]
            