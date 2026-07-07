class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if len(str(num))== 1 :
            return num
        n=0
        for i in range(0,len(str(num))) :
            n=n+num%10
            num=num/10
        return self.addDigits(n)

