class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        deez = len(digits)
        if deez==0:
            return []
        letters = {
            '2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], 
            '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'], '8': ['t', 'u', 'v'], 
            '7': ['p', 'q', 'r', 's'], '9': ['w', 'x', 'y', 'z']
        }
        # if deez==1:
        #     return letters[digits]
        output = ['']
        for i in range(deez):
            output =  [''.join([x,y]) for x in output for y in letters[digits[i]]]
        return output        