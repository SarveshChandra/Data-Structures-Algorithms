class Solution:
    def powerOfFour(self, input):
        '''
        :type input: int
        :rtype: bool
        
        The number 0x55555555 is a 32 bit number with all odd bits set as 1 and all even bits as 0
        We also check if input>0 and input is power of 2

        '''
        alternatingOddBitMask = 0x55555555  # 1010101010101010101010101010101

        isNonZero = input != 0
        hasSingleLeadingOneBit = (input & (input - 1)) == 0
        hasOnlyOddPositionedBits = (input & alternatingOddBitMask) == input

        return isNonZero and hasSingleLeadingOneBit and hasOnlyOddPositionedBits

a = Solution()
b = a.powerOfFour(16)
print(b)