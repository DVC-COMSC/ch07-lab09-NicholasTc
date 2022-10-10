# ******************************
# Make your Code
# ******************************
names = input().split()

shortest = names[0]
longest = names[0]

for name in names:
    if len(name) > len(longest):
        longest = name
    elif len(name) < len(shortest):
        shortest = name
    elif len(name) == len(longest):
        if ord(name[0]) < ord(longest[0]):
            longest = name
    elif len(name) == len(shortest):
        if ord(name[0]) < ord(shortest[0]):
            shortest = name

print(shortest, longest)
