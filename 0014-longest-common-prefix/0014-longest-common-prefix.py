class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = True
        output = []
        f_output = ""
        i = 0
        if not strs:
            return ""
        while prefix == True:
            for x in strs:
                if i >= len(x): 
                    prefix = False
                    break
                output.append(x[i])
            
            if prefix and len(set(output)) == 1:
                f_output += output[0]
                i += 1
            else:
                prefix = False
            output.clear()
        
        return f_output