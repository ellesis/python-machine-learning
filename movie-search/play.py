import requests
import collections

MovieResult = collections.namedtuple(
    'MovieResult',
    'Title, Poster, Type, imdbID, Year'
)

search = 'capital'
url = 'http://www.omdbapi.com/?s={}&apikey=3f8e06be'.format(search)
r = requests.get(url)
data = r.json()

results = data['Search']
# print(len(results))
# print(results[0])

# movie_1 = results[0]
# print(movie_1['Year'])

movies = []
for result in results:
    m = MovieResult(
        Title = result['Title'],
        Poster = result['Poster'],
        Type = result['Type'],
        imdbID = result['imdbID'],
        Year = result['Year']
    )
    # print(m)
    movies.append(m)

print(movies)


