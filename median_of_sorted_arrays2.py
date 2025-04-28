class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i=0
        h=0
        x=[]
        #j=len(nums1)-1
        #k=len(nums1)-1
        while (i<len(nums1)) and (h<len(nums2)):
            # m=(i+j)//2
            if nums1[i]<nums2[h]:
                x.append(nums1[i])
                i+=1
            else:
                x.append(nums2[h])
                h+=1
        while i<len(nums1):
            x.append(nums1[i])
            i+=1
        while h<len(nums2):
            x.append(nums2[h])
            h+=1
        c=len(x)
        v=c//2
        if c%2==0:
            return ((x[v]+x[v-1])/2)
        else:
            return x[v]
        

        