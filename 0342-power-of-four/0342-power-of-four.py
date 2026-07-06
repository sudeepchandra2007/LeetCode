class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n>0 :
            if (math.log(n)/math.log(4)).is_integer()==True :
                return True
        return False