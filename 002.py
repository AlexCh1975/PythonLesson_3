li = [x for x in range(1, 20)]

# li = map(lambda x: x + 10, li) >>> <map object at 0x000000D2F5E0B580>
li = list(map(lambda x: x + 10, li))
# [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
print(li)