class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        if not path:
            return ""
        stack = []
        p = path.split('/')
        print p
        for n in p:
            if n in ("","."):
                continue
            elif n == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(n)
        return '/' + '/'.join(stack)
                
#the reason why there is "" is because if there is multiple "/" next to each other,
#then the substring after split is ""