##### EXERCISES FOR RIDE SCOUT #####
# 1. Sort the list of dicts by 'name' alphabetically
# Return a list of strings using the following format '<name> | <movie>'
# 2. Sort the list of dicts by 'movie'
# Return a dict with the key as the 'movie' and the value is a list of names sorted alphabetically

import pprint

# Would ideally have all this data coming from a file or other form of input,
# but for example's sake, this data set is displayed within the file.
characters = [{
    'name': 'frodo',
    'movie': 'lotr'
}, {
    'name': 'gandolf',
    'movie': 'lotr'
}, {
    'name': 'sam',
    'movie': 'lotr'
}, {
    'name': 'luke',
    'movie': 'star-wars'
}, {
    'name': 'obi-wan',
    'movie': 'star-wars'
}, {
    'name': 'darth vader',
    'movie': 'star-wars'
}, {
    'name': 'picard',
    'movie': 'star-trek'
}, {
    'name': 'kirk',
    'movie': 'star-trek'
}, {
    'name': 'spock',
    'movie': 'star-trek'
}]


def alphabetize(k):
    # "Schwartzian" Perl method
    sort_by = k
    d = [(char_[sort_by], char_) for char_ in characters]
    d.sort()
    result = [char_ for (key, char_) in d]

    new_format = []

    if k == 'name':
        v = 'movie'
    else:
        v = 'name'

    for i in result:
        new_format.append(i[k] + ' | ' + i[v])

    pprint.pprint(new_format)


def sort_movie_chars():
    movies = {}

    # there is probably a cleaner way, than to repeat this chunk.
    sort_by = 'movie'
    d = [(char_[sort_by], char_) for char_ in characters]
    d.sort()
    result = [char_ for (key, char_) in d]

    for i in result:
        if i['movie'] in movies:
            pass
        else:
            movies.update({i['movie']: []})

        if i['movie'] in movies:
            movies[(i['movie'])].append(i['name'])

    pprint.pprint(movies)

# exercise 1
alphabetize('name')

# exercise 2
sort_movie_chars()