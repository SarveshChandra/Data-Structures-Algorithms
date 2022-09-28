class Solution:
    def sortArray_0_1_2(self, nums):
        '''
        :type nums: list of int
        :rtype: list of int
        '''
        #Counting Sort Algorithm
        
        #Make three variables
        #For counting 0,1 and 2 respectively
        c0 = c1 = c2 = 0
        
        #//Iterate through the nums list and count the frequencies of each number
        for num in nums:
            if num == 0:
                c0 += 1
            elif num == 1:
                c1 += 1
            else:
                c2 += 1
                
        #Fill the original array
        #First fill all 0, then 1 and at last 2
        nums[:c0] = [0] * c0
        nums[c0:c0+c1] = [1] * c1
        nums[c0+c1:] = [2] * c2
        
        return nums

a = Solution()
b = a.sortArray_0_1_2([2,2,1,1,1,0,0,0,0])
print(b)