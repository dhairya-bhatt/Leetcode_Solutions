class Solution:
    def checkDivisibility(self, n: int) -> bool:
        d_sum = sum(int(digit) for digit in str(n))
        d_product = 1
        num = n
        while num >= 1:
            d_product *= num % 10  
            num = num//10
        if n%(d_sum+d_product)==0:
            return True
        else:
            return False
        