class Solution(object):
    def isPalindrome(self, s):
        a=s.lower()
        b=" ".join(i for i in a if i.isalnum())
        v=b[:: -1]
        if v==b:
            return True
        else:
            return False        