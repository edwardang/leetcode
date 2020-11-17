class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        remove_start, remove_end = toBeRemoved[0], toBeRemoved[1]
        output = []
        # Can do in one pass O(n) time.
        for start,end in intervals:
            # take this by case.
            
            # bad and confusing code. Comments reference remove range but conditional statement from 
            # start/end perspective
            
            #1) they aren't intersecting with the remove range
            if end < remove_start or start >= remove_end:
                output.append([start,end])
                
            #2) remove range falls in the middle
            elif start < remove_start and end > remove_end:
                output.append([start,remove_start])
                output.append([remove_end, end])
                
            #3) right side of remove range falls inside only.
            elif start >= remove_start and start < remove_end and end > remove_end:
                output.append([remove_end,end])
                
            #4) left side of remove range falls inside only
            elif start < remove_start and end >= remove_start and end < remove_end:
                output.append([start,remove_start])
                
        return output
        