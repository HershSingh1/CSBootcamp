from collections import Counter

# print(Counter("mississippi"))
# print(Counter(["cat", "dog", "cat", "fish"]))
# print(Counter(cat=2, dog=1))
# print(Counter[0])

c = Counter("aabbbcc")
# print(c["a"])
# print(c["s"])
# c.update("abx")
# print(c)
# print(c.most_common())
# c.most_common()
# returns most common items in the dictionary in descending order as tuples
# the argument in most common specifies how many to do (top 2, top 3, etc.)

# print(c)
# c.subtract("aabbbbb")
# print(c)
# print(c.elements)
# print(list(c.elements()))
# print(c.total)

d = Counter("aabcxyz")
print(c)
print(d)
print(c + d)
print(c - d)
print(c & d)
print(c | d)
