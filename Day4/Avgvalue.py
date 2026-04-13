class Solution:
    def averageValue(self, nums: List[int]) -> int:
        sum=0
        count=0
        avg=0
        for i in nums:
            if i%6==0:
                sum+=i
                count+=1
                avg=sum//count
            else:
                avg==0
        return avg
