# Import the Counter class so we can make the Bag easily
from collections import Counter

poem = """Two roads diverged in a yellow wood,
And sorry I could not travel both
And be one traveler, long I stood
And looked down one as far as I could
To where it bent in the undergrowth;"""

# Convert the poem to lowercase, since computers are case sensitive.
poem = poem.lower()

# Break the poem down into words, so we can make a bag at the word level
words = poem.split()

# Make a bag out of the list of words
bag = Counter(words)

print(bag)
