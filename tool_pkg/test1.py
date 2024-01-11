

import typing
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        fast = slow = 1
        while fast < n:
            if nums[fast] != nums[fast - 1]:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1

        return slow,nums[0:slow]

if __name__ == '__main__':
    test1 = Solution()
    ss = test1.removeDuplicates(nums=[0,0,1,1,1,2,2,3,3,4])
    print(ss)