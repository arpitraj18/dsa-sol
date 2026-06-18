class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        output=[0]*len(nums)
        op_index=0
        index=len(nums)
        for ind in range(len(nums)):
            if nums[ind]>0:
                index=ind
                break
        

        for i in range(len(nums)):
            nums[i] **= 2
        neg_index= index-1
        pos_index=index

        while neg_index>=0 and pos_index<len(nums):
            if nums[neg_index]>nums[pos_index]:
                output[op_index]=nums[pos_index]
                op_index+=1
                pos_index+=1
            else:
                output[op_index]=nums[neg_index]
                op_index+=1
                neg_index-=1
        
        while pos_index<len(nums):
            output[op_index]=nums[pos_index]
            op_index+=1
            pos_index+=1

        while neg_index>=0:
            output[op_index]=nums[neg_index]
            op_index+=1
            neg_index-=1
        return output