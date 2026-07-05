class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n>0 :
            for i in range(0,100) :
                if n==pow(3,i) :
                    return True
                elif n<pow(3,i) :
                    return False
        return False