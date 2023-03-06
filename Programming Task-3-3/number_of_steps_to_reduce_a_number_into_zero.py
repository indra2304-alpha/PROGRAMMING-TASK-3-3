class Solution:
    def numberOfSteps(self, num: int) -> int:
        action = {0: lambda x: x // 2, 1: lambda x: x - 1}
        
        step = 0
        while num:
            num = action[num % 2](num)
            step += 1
            
        return step
