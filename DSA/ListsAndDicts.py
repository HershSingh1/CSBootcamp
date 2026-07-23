from collections import defaultdict

# LISTS
fruits = ["apples", "oranges", "bananas", "strawberries", "plums", "peaches"]
fruits.append("mangoes")
vegetables = ["lettuce", "celery", "broccoli", "bell peppers"]
fruits.sort()
fruits.reverse()
# print(fruits)


# DICTIONARIES
capitals = {
    "Canada": "Ottawa",
    "Mexico": "Mexico City",
    "Hungary": "Budapest",
    "Romania": "Sofia",
}
count = capitals.get("Canada", 0)

dict1 = {}
dict1.setdefault("apple", 1)
dict1.setdefault("banana", 1)
dict1["apple"] += 1
# print(dict1)

# DEFAULTDICT
freq = defaultdict(int)
freq["apple"] += 1
freq["banana"] += 1
freq["apple"] += 1
# print(freq)

# PRACTICE
# defaultdict implementation
word = "banana"
# letters = defaultdict(int)
# for letter in word:
#     letters[letter] += 1
# print(letters)

# dictionary implementation
letters2 = {}
for letter in word:
    letters2.setdefault(letter, 0)
    letters2[letter] += 1
# print(letters2)

nums = [5, 7, 3, 7, 1]
numset = set()
for num in nums:
    if num in numset:
        # print(num)
        break
    numset.add(num)


# next problem
l1 = [1, 2, 3]
l2 = [3, 2, 1]

freq1 = defaultdict(int)
freq2 = defaultdict(int)

for num in l1:
    freq1[num] += 1

for num in l2:
    freq2[num] += 1

print(freq1 == freq2)
