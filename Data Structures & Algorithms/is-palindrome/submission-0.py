class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp=''
        #clean up string
        for i in range(len(s)):
            if 97<=ord(s[i])<=122 or "0"<=s[i]<="9":
                temp+=s[i]
            elif 65<=ord(s[i])<=90:
                temp+=s[i].lower()
            else:
                continue
        s=temp
        i=0
        j=len(s)-i-1     
        while(i<j):
            if s[i]!=s[j]:
                return False
            i+=1
            j-=1
        return True
        
