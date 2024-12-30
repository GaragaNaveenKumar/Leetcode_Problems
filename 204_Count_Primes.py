class Solution:
    def countPrimes(self, n: int) -> int:
        if n<=2:
            return 0
        
        primes_count=0
        prime_list=[True]*n
        prime_list[0]=prime_list[1]=False
        for i in range(2,n):
            if prime_list[i]:
                primes_count+=1
                for j in range(i*i,n,i):
                    prime_list[j]=False
        return primes_count