a = [-3, -1, 0, 1, 4, 7]

print("hello")
# # def binarysearch1(arr, target):
# #     l = 0
# #     r = len(arr) - 1
# #     while l <= r:
# #         m = (l + r) // 2
# #         if arr[m] == target:
# #             print(True)
# #             return True
# #         elif arr[m] > target:
# #             r = m - 1
# #         elif arr[m] < target:
# #             l = m + 1
# #     print(False)
# #     return False


# # binarysearch1(a, -1)


# # based on a condition
# b = [False, False, False, False, True, True, True]


# def binarysearchoncondition(arr):
#     n = len(arr)
#     l = 0
#     r = n - 1
#     while (
#         l < r
#     ):  # we need to forefully escape when l = r, since that means we've found the first instance, in normal binary search, we will naturally escape by either crisscrossing or finding the value of m
#         m = (l + r) // 2
#         if b[m]:
#             r = m  # we do this since we don't know if l is safe, l could be the last false for example
#         else:
#             m = l + 1
#     print(l)  # we can print l or r since in the end they should be in the same place
#     return l


# # THEY MAKE MAKE YOU USE m = l + (r-1)//2 INSTEAD

# binarysearchoncondition(b)
