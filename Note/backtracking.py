#Combination:

nums = [...]
res = []

# C(m, n)
def dfs(self,nums, start, tmp, res):
    res.append(tmp[:]) #copy
    for i in range(start, len(nums)):
        tmp.append(nums[i])
        self.dfs(nums, i+1, tmp, res)
        tmp.pop()

self.dfs(nums,0,[], res)
return res


#Permutation: consider order
nums = [...]
ans  = []
used = [False] * len(nums)

#P(m, n)
def dfs(n, cur):
	if len(curr) == n:
		ans.append(curr)
		return

	for i in range(len(nums)):
		if used[i]:
			continue
		used[i] = True
		curr.append(nums[i])
		self.dfs(n, curr)
		curr.pop()
		used[i] = False

for i in range(len(nums)):
	self.dfs(i, 0 [])
