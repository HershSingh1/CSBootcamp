# o(n)
# no need for defaultdict but it works
# defaultdict only used if a default value is needed to be inserted if you check if a key exists but it doesnt actually exist
# the key is to create a dictionary since lookup is done in o(1) time "have i seen this before"
# then you should have the key and value be the value of in the list and the index, making it easier to access that information
# complement is also important as a checking mechanism for addition

from collections import defaultdict


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = defaultdict(int)

        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in seen:
                return [seen[complement], i]

            seen[nums[i]] = i
