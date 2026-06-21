class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """

        
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
 
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX
     
        negative = (dividend < 0) != (divisor < 0)
        
        dvd = abs(dividend)
        dvs = abs(divisor)
        
        result = 0
        
        while dvd >= dvs:
            temp = dvs
            multiple = 1
            
            while dvd >= (temp << 1):
                temp <<= 1
                multiple <<= 1
            
            dvd -= temp
            result += multiple
        
        return -result if negative else result