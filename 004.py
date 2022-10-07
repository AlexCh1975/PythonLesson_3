# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [4, 5, 9, 14, 7]

# # data = zip(users, ids) # <zip object at 0x000000617AE41340>
# data = list(zip(users, ids)) # [('user1', 4), ('user2', 5), ('user3', 9), ('user4', 14), ('user5', 7)]

# print(data)

############################################################################

users = ['user1', 'user2', 'user3', 'user4', 'user5']
ids = [4, 5, 9, 14, 7]
salary = [111, 222, 333]

data = list(zip(users, ids, salary)) # [('user1', 4, 111), ('user2', 5, 222), ('user3', 9, 333)]

print(data)