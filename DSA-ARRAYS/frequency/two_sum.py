class solution:
    def twoSum(self,nums,target):
        seen ={}

        for i in range(len(nums)):
            number = nums[i]
            needed = target-number

            if needed in seen:
                return[seen[needed],i]
            seen[number]=i


nums = [2,7,11,15]
target =18

solution=solution()
print(solution.twoSum(nums,target))

