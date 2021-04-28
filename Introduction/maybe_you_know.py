usersList = [
    {"id": 0, "name": "Jonas"},
    {"id": 1, "name": "Luana"},
    {"id": 2, "name": "Eduardo"},
    {"id": 3, "name": "Fábio"},
    {"id": 4, "name": "Giulia"},
    {"id": 5, "name": "Bruna"},
    {"id": 6, "name": "Robert"},
    {"id": 7, "name": "Cleiton"},
    {"id": 8, "name": "Thor"},
    {"id": 9, "name": "Kelin"},
]

friendships = [(0, 1), (0, 2),(1, 2), (1, 3), (2, 3),
               (3, 4), (4, 5), (5, 6), (5, 7),(7, 8), (8, 9)]

# Configuração lsita de amigos para cada usuário
for user in usersList:
  user["friends"] = []

# Povoando lista de amigos
for i, j in friendships:
  # Isso funciona porque users[i] é igual ao id do user
  usersList[i]["friends"].append(j)
  usersList[j]["friends"].append(i)

def friends_of_friend_ids_bad(user):
  # foaf = friend of a friend
  return [usersList[foaf]["id"]
          for friend in user["friends"]
            for foaf in usersList[friend]["friends"]]


def is_not_the_same_user(user, other_user):
    return user["id"] != other_user["id"]


def is_not_a_friend(user, other_user):
    # other_user não é um amigo se não está em user["friends"]
    return all(is_not_the_same_user(usersList[friend], other_user)
               for friend in user["friends"])


def friends_of_friend_ids_good(user):
    from collections import Counter

    return Counter(usersList[foaf]["name"]
                for friend in user["friends"]
                    for foaf in usersList[friend]["friends"]
                        if is_not_a_friend(user, usersList[foaf])
                            and is_not_the_same_user(user, usersList[foaf]))


print(f"User {usersList[0]['name']} has  commons friends with {friends_of_friend_ids_good(usersList[0])}.")