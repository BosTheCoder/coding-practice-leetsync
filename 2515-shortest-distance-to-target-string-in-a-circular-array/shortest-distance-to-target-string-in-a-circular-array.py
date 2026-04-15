class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        targetIndices = [ix for ix,word in enumerate(words) if word==target]
        if len(targetIndices) == 0:
            return -1
        
        min_distance = float(inf)
        for targetIndex in targetIndices:
            # Calculate distance if going right from startindex
            rightDistance = targetIndex - startIndex if targetIndex>=startIndex else (targetIndex+len(words))-startIndex
            # Calculated distance if going left from startIndex
            leftDistance = startIndex - targetIndex if startIndex>=targetIndex else startIndex - (targetIndex -len(words))

            min_distance = min(min_distance, leftDistance, rightDistance)

        return min_distance

