class Solution:
    def isValid(self, s: str) -> bool:
        list = []
        pairs = {")":"(", "]":"[", "}":"{"}
        for i in s:
            if i in "{([":
                list.append(i)
            else:
                if len(list)==0 or list.pop() != pairs[i]:
                    return False
        return not list

