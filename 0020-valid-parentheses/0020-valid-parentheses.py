from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        length = len(s)
        if length%2 != 0:
            return False
        else:
            stack = deque()
            for x in s:
                if x in "[({":
                    if x =="[":
                        stack.append("]")
                    elif x == "{":
                        stack.append("}")
                    elif x == "(":
                        stack.append(")")
                elif x in "})]":
                    if not stack:
                        return False
                    elif x != stack[-1]:
                        return False
                    else:
                        stack.pop()
                else:
                    return True
            if not stack:
                return True
            else:
                return False

       

