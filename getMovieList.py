##get a list of top 100 movies from imdb

import requests
import json

imdbKey = "k_aaaaaaaa"
imdbAPIURL = "imdb-api.com"

# topMovies = requests.get('http://' + imdbAPIURL + '/en/API/Top250Movies/' + imdbKey)


# ##save as json file
# with open('topMovies.json', 'w') as outfile:
#     json.dump(topMoviesJson, outfile)

topMoviesJson = json.load(open('topMovies.json'))

##get a list of just titles
topMovies = []
for movie in topMoviesJson['items']:
    topMovies.append(movie['fullTitle'])
print(topMovies)

##save top movies as text tile
with open('topMovies.txt', 'w') as outfile:
    for movie in topMovies:
        outfile.write(movie + '\n')
        