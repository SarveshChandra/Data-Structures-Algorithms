class Solution:
    def addStrings(self, s1, s2):
        '''
        :type s1: str
        :type s2: str
        :rtype: str
        '''
        i = len(s1) - 1
        j = len(s2) - 1
        carry = 0
        result = ""

        # Start from the end of the string to simulate the addition process
        while i >= 0 or j >= 0:
            sum = carry

            # If we still have digits to examine in s1, then add to sum
            if i >= 0:
                sum += ord(s1[i]) - ord('0')
                i -= 1
            # If we still have digits to examine in s2, then add to sum
            if j >= 0:
                sum += ord(s2[j]) - ord('0')
                j -= 1

            # Updates carry and adds to the result string
            carry = int(sum / 10)
            result += str(sum % 10)

        # If we have a carry leftover, then add it to the result
        if carry != 0:
            result += str(carry)

        # Since we are adding the digits in reverse order, we must reverse our resultant string to obtain the final answer
        return result[::-1]

a = Solution()
b = a.addStrings('1','2')
print(b)