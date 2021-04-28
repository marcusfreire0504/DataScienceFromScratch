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

def number_of_friends(user):
  return len(user["friends"])

total_connections = sum(number_of_friends(user) for user in usersList)
avg_connections = total_connections / len(usersList)


number_of_friends_by_id = [(user["id"], number_of_friends(user)) for user in usersList]


sorted(number_of_friends_by_id,
       key=lambda user : user[1],
       reverse=True)
print(f"Total: {total_connections}\n"
      f"Average: {avg_connections}")


