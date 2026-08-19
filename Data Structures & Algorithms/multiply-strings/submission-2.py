class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1=0
        n2=0
        for i in range(len(num1)):
            temp=self.returnDigit(num1[i])
            n1+=temp*(10**(len(num1)-i-1))
        for i in range(len(num2)-1,-1,-1):
            temp=self.returnDigit(num2[i])
            n2+=temp*(10**(len(num2)-i-1))
        return str(n1*n2)


    def returnDigit(self,n):
        match n:
            case '0':
                return 0
            case '1':
                return 1
            case '2':
                return 2
            case '3':
                return 3
            case '4':
                return 4
            case '5':
                return 5
            case '6':
                return 6
            case '7':
                return 7
            case '8':
                return 8
            case '9':
                return 9

