# time complexity = o(n)


class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        numset = set()
        for num in nums:
            if num in numset:
                return True
            numset.add(num)
        return False


from collections import defaultdict


class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        numdict = defaultdict(int)
        for num in nums:
            numdict[num] += 1
            if numdict[num] == 2:
                return True
        return False
