import math
class Solution:
    def changeBase(self, numAsString, b1, b2):
        '''
        :type numAsString: str
        :type b1: int
        :type b2: int
        :rtype: str
        '''
        is_negative = numAsString[0] == "-"
        start = 1 if is_negative else 0
        max_power = len(numAsString) - 1
        number_under_base_10 = 0
        for i in range(start, len(numAsString)):
            # Extract digit symbol and determine if it is a number or letter
            character = numAsString[i]
            is_place_a_digit = self.is_number(character)
            # Convert digit or letter into integer value
            value_contributed_by_place = int(
                character) if is_place_a_digit else (ord(character) - ord('A') + 10)
            position_power_weight = max_power - i
            number_under_base_10 += math.floor(
                value_contributed_by_place * math.pow(b1, position_power_weight))
        if number_under_base_10 == 0:
            return "0"
        else:
            return ("-" if is_negative else "") + self.base_10_to_new_base(number_under_base_10, b2)
    def base_10_to_new_base(self, number_under_base_10, base):
        if number_under_base_10 == 0:
            return ""
        # lsd -> "Least Significant Digit"
        lsd_as_char = ""
        lsd_under_final_base = number_under_base_10 % base
        needs_hex_conversion = True if lsd_under_final_base >= 10 else False
        if needs_hex_conversion:
            ascii_value = ord('A') + lsd_under_final_base - 10
            lsd_as_char = chr(ascii_value)
        else:
            lsd_as_char = str(int(lsd_under_final_base))
        base_10_number_without_lsd = number_under_base_10 // base
        everything_else_to_our_left = self.base_10_to_new_base(
            base_10_number_without_lsd, base)
        return everything_else_to_our_left + lsd_as_char
    def is_number(self, s):
        try:
            float(s)
            return True
        except ValueError:
            pass
        return False
    
a = Solution()
b = a.changeBase("12", 10, 2)
print(b)