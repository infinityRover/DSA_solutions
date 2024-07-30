class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter={}
        for num in nums:
            if num in counter:
                counter[num]+=1
            else:
                counter[num]=1

        max_count=-1
        val=-1
        for key, value in counter.items():
            if max_count<value:
                max_count=value
                val=key
        return val
    

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans=-1
        count=0
        for num in nums:
            if count==0:
                ans=num
            if ans==num:
                count+=1
            else:
                count-=1
        return ans