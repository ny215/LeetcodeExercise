class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = version1.split(".")
        v2 = version2.split(".")
        for i in range(max(len(v1), len(v2))):
            if len(v1) <= i:
                ver1 = 0
            else:
                ver1 = v1[i]
                
            if len(v2) <= i:
                ver2 = 0
            else:
                ver2 = v2[i]
                
            if int(ver1) < int(ver2):
                return -1
            elif int(ver1) > int(ver2):
                return 1
        return 0
