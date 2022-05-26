class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        G = defaultdict(lambda:set())
        n = len(beginWord)
        for i in wordList:
            for j in range(len(i)):
                G[j].add(i[j])
        #print(G)
        Q = [(beginWord,1)]
        bag = set(wordList)
        bag.add(beginWord)
        visit = set()
        if endWord not in bag:
            return 0
        while Q:
            s,c = Q.pop(0)
            #print(s)
            if s==endWord:
                return c
            if s not in bag:
                continue
            for i in range(n):
                curr = s[i]
                for j in G[i]:
                    if j!=curr:
                        new = s[:i] + j + s[i+1:]
                        if new not in visit:
                            visit.add(new)
                            Q.append((new,c+1))
        return 0
                    
            