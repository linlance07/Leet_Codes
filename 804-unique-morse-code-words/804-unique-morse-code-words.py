class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        S = set()
        for i in words:
            s = ""
            for j in i:
                s += morse[ord(j)-97]
            #print(s)
            S.add(s)
        return len(S)
                