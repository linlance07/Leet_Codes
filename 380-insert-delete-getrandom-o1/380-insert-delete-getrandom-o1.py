class RandomizedSet:

    def __init__(self):
        self.S = set()
    def insert(self, val: int) -> bool:
        pres = len(self.S)
        self.S.add(val)
        if len(self.S)==pres:
            return False
        return True

    def remove(self, val: int) -> bool:
        try:
            self.S.remove(val)
            return True
        except:
            return False

    def getRandom(self) -> int:
        return random.choice(list(self.S))
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()