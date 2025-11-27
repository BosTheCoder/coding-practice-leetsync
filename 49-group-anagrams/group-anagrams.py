class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ret = defaultdict(list)
        for s in strs:
            d = Counter(s)
            d = tuple(sorted(tuple(d.items())))
            ret[d].append(s)
        
        return list(ret.values())
        
        # ret[tuple({"a":1,"b":2})].append(1)
        # ret[tuple({"b":2,"a":1})].append(1)
        # print(ret)