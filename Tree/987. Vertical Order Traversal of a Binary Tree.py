class Solution(object):
    def verticalTraversal(self,root):
        dic = collections.defaultdict(list)
        queue  = collections.deque([(root,0 , 0)])
        ans = []
        while queue:
            node, level, depth = queue.popleft()
            if node:
                dic[level].append((depth, node.val))
                queue.append((node.left, level-1 ,depth -1))
                queue.append((node.right, level+1, depth -1))
                
        for i in sorted(dic.keys()):
            level = [x[1] for x in sorted(dic[i], key= lambda x: (-x[0], x[1]))]
            ans.append(level)
        return ans