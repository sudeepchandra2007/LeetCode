class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        for i in range(len(s)-1,-1,-1) :
            if not s[i].isalnum() :
                s=s[:i] + "" + s[i+1:]
        s=s.lower()
        for i in range(0,len(s)/2) :
            if not s[i]==s[len(s)-i-1] :
                return False
        return True

                