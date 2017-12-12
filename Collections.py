# Collections
# String: str
# Bytes: bytes
# Arrays: list
# Dictionary: dict

# 1) Strings: Immutable sequence of unicode codepoints
# Single and double quotes
h = 'This is a string """yay"""'
print(h)

h = "This is a string with double quotes '''yay'''"
print(h)

# Multiline strings: triple double or single quotes

h = """This is a 
long multi line
string"""
print(h)

m = "This\\ is\nmulti\nline"
print(m)

# Raw strings
path = r'C:\User\Documents\Books'
print(path)

# String as sequences
s = "parrot"
print(s[0])
print(s[4])

# Use the type() function to get the object's type
print(type(s))

print(s.capitalize())
print(s.upper())

# Bytes: similar to strings, but instead of a sequence
# of Unicode points is a sequence of bytes.
# use for raw binary data, fixed-width, ASCII

bt = b'data for bytes'
print(bt.split())

# Encode data: utf-8
# ó = Alt+162
l = "Visitamos el zoológico"
print(l)
data = l.encode("utf-8")
print(data)
s = data.decode("utf-8")
print(s)

# List - aka array, a list of mutable objects
# Replace, remove, or append elements
# Delimited by [], and items are separated by commas
l = [1, 2, 3]
print(l)
print(type(l))
a = ["apple", "orange", "pear"]
print(a[1])
b = ["Waldo", 2, 4.5]
print(b)

ll = ["apple", "john", [1, 2, 3]]
print(ll[2][1])

c = ["bear",
     "horse",
     "elephant",]

print(c)