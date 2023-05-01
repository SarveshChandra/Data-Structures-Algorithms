class Solution:
    def reverseBits(self, input):
        '''
        :type input: int
        :rtype: int
         
     * Approach:
     *   1. Check the last bit of input
     *   2. Shift output left
     *   3. If it is 1, add it to output (do nothing otherwise)
     *   4. Shift input right
     *
     * Stop when input is 0
     

        '''
        output = 0

        while input != 0:
            output = output << 1

            if input & 1 == 1:
                output |= 1

            input = input >> 1

        return output

a = Solution()
b = a.reverseBits(1112)
print(b)