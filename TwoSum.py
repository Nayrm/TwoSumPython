#Given an array of integers nums and an integer target,
#return indices of the two numbers such that they add up to target.

#Only one valid solution per set


class Solution:
    def twoSum(self,nums, target):
        differences = {}
        #Differences dictionary/hashamp to store the difference between our nums and the target
        for i, num in enumerate(nums):
            difference = target - num
            if difference in differences:
                #Check if the difference is in our dictionary
                return [differences[difference], i]
            else:
                differences[num] = i
                #Add curent num and its index to our dictionary
        print(differences)
        return []

solution = Solution()
nums = [2,7,11,15]
target = 9
print(solution.twoSum(nums, target))