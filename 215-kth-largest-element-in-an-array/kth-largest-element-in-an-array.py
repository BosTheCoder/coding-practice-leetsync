class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def dfs(arr:list, v):
            pivot = random.choice(arr)
            # print(arr, "k",v, "pivot", pivot)
            greater, equal, smaller = [], [], []
            for num in arr:
                if num >pivot:
                    greater.append(num)
                elif num == pivot:
                    equal.append(num)
                else:
                    smaller.append(num)
            # print(greater, equal, smaller)
            if v <= len(greater):
                return dfs(greater, v)
            elif v > len(greater) + len(equal):
                return dfs(smaller, v-len(greater)-len(equal))
            else:
                return equal[0]
        return dfs(nums, k)



