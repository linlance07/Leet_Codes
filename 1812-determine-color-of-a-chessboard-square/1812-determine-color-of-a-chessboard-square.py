class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        a = ord(coordinates[0])-96
        b = int(coordinates[1])
        if (a+b)%2==0:
            return False
        return True