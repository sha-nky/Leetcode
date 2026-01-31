class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if not letters:
            return ""
        
        minOrd = float("inf")
        flag = 0
        for char in letters:
            if ord(char) > ord(target):
                minOrd = min(minOrd, ord(char))
                flag = 1
        
        return chr(minOrd) if flag else letters[0]
