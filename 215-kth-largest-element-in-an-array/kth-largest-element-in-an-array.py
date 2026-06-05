class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        arr = nums
        while arr:
            pivot = random.choice(arr)
            print(pivot)

            left = []
            middle = []
            right = []
            for num in arr:
                if num<pivot:
                    left.append(num)
                elif num == pivot:
                    middle.append(num)
                else:
                    right.append(num)
            
            print(left, middle, right)
            if k<=len(right):
                arr=right
            elif k<=(len(right)+len(middle)):
                return middle[0]
            else:
                arr=left
                k = k - len(middle) - len(right)
        raise ValueError()



"""

choose random number
4
split it

left = 3,2,1    aka less than 
middle = 4      aka equal to
right = 5,6     aka greater than

we know that 4 is the 3rd largest
if k is < 3 we need to look in right
if k is > 3 we need to look in left

it's 1 indexed



"""