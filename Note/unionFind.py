"""
union find
Find(x): find the root/cluster-id of x
Union(x, y): merge two clusters
check wheter two elements are in the same set or not in O(1) amortized
"""
class UnionFindSet:
	def __init__(self):
		self.parent = range(1001)
		self.rank =[0] * 1001

	def find(self, x):
		if x != self.parent[x]:
			self.parent[x] = self.find(self.parent[x])
		return self.parent[x]

	def union(self, x, y):
		xr, yr = self.find(x), self.find(y)
		if xr == yr:
			return False
		elif self.rank[xr] < self.rank[yr]:
			self.parent[xr] = yr
		elif self.rank[xr] > self.rank[yr]:
			self.parent[yr] = xr
		else:
			self.parent[yr] = xr
			self.rank[xr] += 1
		return True