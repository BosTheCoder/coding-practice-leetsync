class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            sorted_s = str(sorted(s))
            temp = d.get(sorted_s,[])
            temp.append(s)
            d[sorted_s] = temp

        # go through all keys and put those in new lists of values

        ret = []
        for k, v in d.items():
            ret.append(v)
        
        return ret