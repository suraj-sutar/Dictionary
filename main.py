# Dictionary allows to store key and values
# how to write it

# friends = {"suraj":21,"kashinath":23,"chetan":26}

# print(friends)
# print(type(friends))

# how to add elements in the dictionary
# you want to add any elements in the dictionary you do not use any keyword like append or add

# friends = {"suraj":21,"kashinath":23,"chetan":26}

# friends["prayag"] = 20

# you alose update the value that is present in the dictionary
# in dictionary do not have any duplicat value or elements
# friends["suraj"] = 22
# friends["suraj"] = 22

# print(friends)

# friends = ({
#   "name": "suraj",
#   "age": 24
# }, {
#   "name": "kashinath",
#   "age": 23
# }, {
#   "name": "prajwal",
#   "age": 20
# })
# print(friends[0]["name"])
# print(friends[1]["name"])
# print(friends[2]["name"])

# in above example friends[0] is a elements number present in the tuple and name is which value you want you also access age value using you can pass friends[0]["age"]....


# dict function it is used to convert the data into dictionary formate

# friends = [("suraj",21), ("kashinath",23),("prayag",21)]
# # in above example i create a list that contains three tuples this list is convert it into dictionary formate using dict function

# new_dictionary = dict(friends)
# print(new_dictionary)
# print(type(new_dictionary))

# my_friends = {
#     'Jose': {'last_seen': 6},
#     'Rolf': {'surname': 'Smith'},
#     'Anne': 6
# }

# my_friends['Jose']['last_seen']
players = [
    {
        'name': 'Rolf',
        'numbers': (13, 22, 3, 6, 9)
    },
    {
        'name': 'John',
        'numbers': (22, 3, 5, 7, 9)
    }
]
print(players[0]['numbers'])
print(players[0]['numbers'][0])