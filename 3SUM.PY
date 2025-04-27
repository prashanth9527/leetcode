class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # i=0
        # nums.sort()
        j=len(nums)
        x=set()
        for i in range(j):
            for h in range(i+1,j):
                for k in range(h+1,j):
                    if nums[i]+nums[h]+nums[k]==0:
                        y=tuple(sorted([nums[i],nums[h],nums[k]]))
                        x.add(y)
        return [list(tr) for tr in x]


        