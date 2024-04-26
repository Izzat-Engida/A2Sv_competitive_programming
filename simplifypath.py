class Solution:
    def simplifyPath(self, path: str) -> str:
        array=[]
        for i in path.split('/'):
            if i=='..':
                if array:
                    array.pop()
            elif i and i!='.':
                array.append(i)
        array='/'.join(array)
        array='/'+array
        return array        
