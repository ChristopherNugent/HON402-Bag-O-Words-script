poem = """Two roads diverged in a yellow wood,
And sorry I could not travel both
And be one traveler, long I stood
And looked down one as far as I could
To where it bent in the undergrowth;"""

# Convert the poem to lowercase, since computers are case sensitive.
poem = poem.lower()

# Split the poem into words and sort those alphabetically
words = sorted(poem.split())

print(words)
