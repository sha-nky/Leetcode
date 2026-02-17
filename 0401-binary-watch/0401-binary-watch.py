class Solution:
    def readBinaryWatch(self, turnedOn: int):
        ans = []
        
        for hr in range(12):
            for mnt in range(60):
                if hr.bit_count() + mnt.bit_count() == turnedOn:
                    ans.append(f"{hr}:{mnt:02d}")
        
        return ans
