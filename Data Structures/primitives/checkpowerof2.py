class Solution:
    def powerOfTwo(self, input):
        '''
        :type input: int
        :rtype: bool
        
        
        Approcah-
        If input is power of 2 than it will have only 1 set bit
        (input-1) will have all other set bits except the original .
        For eg 8- 1000 and 7- 0111
        So their bitwise & results to 0


        '''
        return input > 0 and (input & (input - 1)) == 0

a = Solution()
b = a.powerOfTwo(128)
print(b)