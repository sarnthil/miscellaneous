import json

i_want_it_as_a = 'dictionary' #alternatively: 'list'

if i_want_it_as_a == 'dictionary':
    authors = dict()
else:
    authors = list()

def readJSON(filename):
    with open(filename) as f:
        for line in f:
            yield json.loads(line)

for book in readJSON("47000_metadata.json"):
    if i_want_it_as_a == 'dictionary':
        authors[book['gutenberg_id']] = [author['display_name'] for author in book['authors']]
    else:
        for author in book['authors']:
            authors.append(author['display_name'])

print("Done.")
input()
print(authors)
