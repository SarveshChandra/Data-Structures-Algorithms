import math

class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x <= 0:
            return x == 0

        logarithm_answer = math.log10(x)
        total_digits = math.floor(logarithm_answer) + 1
        msd_mask = math.pow(10, total_digits - 1)

        for i in range(int(total_digits) // 2):
            most_significant_digit = x // msd_mask
            ones_place_digit = x % 10

            if most_significant_digit != ones_place_digit:
                return False

            x %= msd_mask  # Remove most significant digit of x
            x //= 10  # Remove last significant digit of x

            msd_mask //= 100  # Remove 2 0's from the mask since we just removed 2 digits

        return True

a = Solution()
b = a.isPalindrome(1112)
print(b)