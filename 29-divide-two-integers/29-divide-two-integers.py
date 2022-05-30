class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend==-2147483648:
            if divisor==-1:
                return 2147483647
        if (dividend<0 or divisor<0) and not (divisor<0 and dividend<0):
            return -(int(math.ceil(abs(dividend)//abs(divisor))))
        return int(math.ceil(abs(dividend)//abs(divisor)))
        #HardCode XD