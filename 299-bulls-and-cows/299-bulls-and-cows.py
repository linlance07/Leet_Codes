class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        B = defaultdict(int)
        bull = 0
        arr = []
        for i in range(len(secret)):
            if secret[i]==guess[i]:
                bull += 1
            else:
                arr.append(guess[i])
                B[secret[i]] += 1
        cow = 0
        for j in arr:
            if j in B:
                B[j] -= 1
                if B[j]==0:
                    del B[j]
                cow += 1
        return str(bull) + 'A' + str(cow) + 'B'