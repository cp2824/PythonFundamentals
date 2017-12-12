
c = ["bear",
     "horse",
     "elephant",]

print(c)

# Add members

c.append("giraffe")

print(c)

b = []
b.append(1)

print(b)

# list constructor: list()
m = list("Characters")
print(m)
m.insert(2, "bird")
print(m)

# Dictionaries - like a hash table, use a key-word to look up a value
# Dictionaries: Mutable mapping of keys to values
# Values are not in any particular order
# {k1: v1, k2: v2}
d = {'alice':'810-789-4562', 'pedro':'956-123-7845'}
print(type(d))
print(d)

# Access a member
print(d['alice'])
# Update a member's value
d['alice'] = '801-789-4562'
print(d)
# if value exists, it is updated.  If not it will add it.
d['new friend'] = '820-367-3423'
print(d)

# For Loops: visit each item in an iterable series
cities = ["London", "Madrid", "Paris", "Ogden"]
for city in cities:
    print(city)

# Access members of dictionary, a for loop gets the key value
for i in d:
    print(i, "=>", d[i])