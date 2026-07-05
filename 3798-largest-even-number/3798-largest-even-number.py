class Solution(object):
    def largestEven(self, s):
        """
        :type s: str
        :rtype: str
        """
        l=len(s)
        inp=int(s)
        for i in range(0,l) :
            if inp%2==0 :
                return str(inp)
            else :
              inp = inp/10
        return ""