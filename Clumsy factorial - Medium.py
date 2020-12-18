################################################################################
#Normally, the factorial of a positive integer n is the product of all positive integers less than or equal to n.  For example, factorial(10) = 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1.
#
#We instead make a clumsy factorial: using the integers in decreasing order, we swap out the multiply operations for a fixed rotation of operations: multiply (*), divide (/), add (+)
#and subtract (-) in this order.
#
#For example, clumsy(10) = 10 * 9 / 8 + 7 - 6 * 5 / 4 + 3 - 2 * 1.  However, these operations are still applied using the usual order of operations of arithmetic:
#we do all multiplication and division steps before any addition or subtraction steps, and multiplication and division steps are processed left to right.
#
#Additionally, the division that we use is floor division such that 10 * 9 / 8 equals 11.  This guarantees the result is an integer.
#
#Author: Mihai Ilas
#
#################################################################################

class Solution:
    def clumsy(self, N: int) -> int:
        if N == 1: return 1
        if N == 2: return 2
        if N == 3: return 6
        
        factorial = int(N*(N-1)/(N-2)+(N-3))
        i = N-4
        rest = N % 4
        
        while(i >= rest+4):
            factorial -= int((i)*(i-1)/(i-2))
            factorial += i-3
            i -= 4
      
        if i == 3:factorial -= 6
        if i == 2: factorial -= 2
        if i == 1: factorial -= 1
        
        return factorial
