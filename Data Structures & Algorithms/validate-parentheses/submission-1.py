class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for bracket in s:
            if bracket in '([{':
                stack.append(bracket)
            else:
                if(len(stack)!=0):
                    last=stack.pop()
                    if last=='(' and bracket==')':
                        continue
                    elif last=='{' and bracket=='}':
                        continue
                    elif last=='[' and bracket==']':
                        continue
                    else:
                        return False
                else:
                    return False
        return len(stack) == 0