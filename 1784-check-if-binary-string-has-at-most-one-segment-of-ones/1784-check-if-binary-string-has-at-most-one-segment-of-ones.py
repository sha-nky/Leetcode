class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        # count = sum(1 for seg in s.split("0") if seg)
        # return count == 1


        return "01" not in s
