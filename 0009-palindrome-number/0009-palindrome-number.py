class Solution(object):
    def isPalindrome(self, x):
        inp=str(x)
        mid=len(inp)/2
        ret=True
        for i in range(0,mid) :
            if inp[i]== inp[len(inp)-i-1] :
                ret=True
            else :
                return False
        return ret