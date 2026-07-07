class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        for i in range(0,len(t)) :
            if s.count(t[i])==0 or s.count(t[i])-t.count(t[i])!=0:
                return t[i]