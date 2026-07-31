# contains duplicate
from collections import defaultdict


class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        answer = set()
        for num in nums:
            if num in answer:
                return True
            answer.add(num)
        return False


# validanagram solution

from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        anagramdict = defaultdict(int)
        for l1 in s:
            anagramdict[l1] += 1
        for l2 in t:
            anagramdict[l2] -= 1
        if all(x == 0 for x in anagramdict.values()):
            return True
        return False


# two sum solution
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        answer = {}
        for i in range(len(nums)):
            if target - nums[i] in answer:
                return [answer[target - nums[i]], i]
            answer[nums[i]] = i


# groupanagrams solution
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        answer = {}
        for str in strs:
            count = [0] * 26
            for letter in str:
                count[ord(letter) - ord("a")] += 1
        if tuple(count) in answer:
            answer[tuple(count)].append(str)
        answer[tuple(count)] = [str]
        return list(answer.values())
