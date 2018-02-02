# time complexity : O(n)
# space complexity: O(n)

class Solution(object):
    def twoSum(self, nums, target):
        num_dict = {}
        for index, number in enumerate(nums):
            if number in num_dict:
                return [num_dict[number], index]
            else:
                num_dict[target - number] = index