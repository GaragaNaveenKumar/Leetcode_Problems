class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        total_set = 0
        for i in range(32):
            total_set += (num2 >> i) & 1

        x = [0] * 32

       
        for i in range(31, -1, -1):
            if (num1 >> i) & 1 and total_set:
                x[i] = 1
                total_set -= 1

        for i in range(32):
            if not x[i] and total_set:
                x[i] = 1
                total_set -= 1

        
        res = 0
        for i in range(32):
            if x[i]:
                res += 2 ** i

        return res
        