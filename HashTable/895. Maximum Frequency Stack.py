class FreqStack(object):

    def __init__(self):
        self.freq = collections.Counter()
        self.m = collections.defaultdict(list)
        self.maxf = 0

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        freq = self.freq
        m = self.m
        freq[x] += 1
        self.maxf = max(self.maxf, freq[x])
        m[freq[x]].append(x)
    
    
    def pop(self):
        """
        :rtype: int
        """
        freq = self.freq
        m = self.m
        maxf = self.maxf
        x = m[maxf].pop()
        if not m[maxf]:
            self.maxf = maxf -1
        freq[x] -= 1
        return x
            



# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()