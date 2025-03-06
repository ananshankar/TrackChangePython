names = 'bob julian tim martin rod sara joyce nick beverly kevin'.split()
ids = range(len(names))
users = dict(zip(ids, names))  # 0: bob, 1: julian, etc

friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3),
               (3, 4), (4, 5), (5, 6), (5, 7), (5, 9),
               (6, 8), (7, 8), (8, 9)]


def get_friend_with_most_friends(friendships=friendships, users=users):
   """Receives the friendships list of user ID pairs,
      parse it to see who has most friends, return a tuple
      of (name_friend_with_most_friends, his_or_her_friends)"""
   # most friends
   friends = {}
   for user1, user2 in friendships:
      friends[user1] = friends.get(user1, 0) + 1
      friends[user2] = friends.get(user2, 0) + 1
   user = max(friends, key=friends.get)
   
   # friends list
   friend_list = []
   for user1, user2 in friendships:
      if user1 == user and user2 not in friend_list:
         friend_list.append(users[user2])
      elif user2 == user and user1 not in friend_list:
         friend_list.append(users[user1])
   
   expected_output = (users[user], friend_list)
   return users[user], friends