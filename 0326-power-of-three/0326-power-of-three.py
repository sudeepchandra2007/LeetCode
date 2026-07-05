class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n>0 :
            for i in range(0,100) :
                j=pow(3,i)
                if n==j :
                    return True
                elif n<j :
                    return False
        return False