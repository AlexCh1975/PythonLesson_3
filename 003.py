# map()

# # data = map(int, input().split())
# # >>> <map object at 0x0000000A691CADD0>
# data = list(map(int, input().split()))
# # >>> [1, 3, 5, 78, 98]
# print(data)

# filter()

data = [x for x in range(10)]

# res = filter(lambda x: not x % 2, data) # <filter object at 0x0000001D0B0FB580>
res = list(filter(lambda x: not x % 2, data)) # [0, 2, 4, 6, 8]

print(res)