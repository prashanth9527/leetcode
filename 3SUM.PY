class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        x = []
        nums.sort()
        i = 0
        while i < len(nums):
            if i > 0 and nums[i] == nums[i-1]:
                i += 1
                continue
            a = nums[i]
            k = i + 1
            j = len(nums) - 1
            while k < j:
                re = a + nums[k] + nums[j]
                if re == 0:
                    x.append([a, nums[k], nums[j]])
                    k += 1
                    j -= 1
                    while k < j and nums[k] == nums[k-1]:
                        k += 1
                    while k < j and nums[j] == nums[j+1]:
                        j -= 1
                elif re > 0:
                    j -= 1
                else:
                    k += 1
            i += 1
        return x
