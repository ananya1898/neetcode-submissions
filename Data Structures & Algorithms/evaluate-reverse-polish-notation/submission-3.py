class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for x in tokens:
            if x in ["+","-","*","/"]:
                a=int(stack.pop())
                b=int(stack.pop())
                if x=="+":
                    stack.append(b+a)
                elif x=="-":
                    stack.append(b-a)
                elif x=="*":
                    stack.append(b*a)
                else:
                    stack.append(int(b/a))
            else:
                stack.append(int(x))
        return (stack.pop())

        