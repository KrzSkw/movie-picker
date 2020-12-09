from get_IMDB_Top import getTopList

TopMovies = getTopList()
print(TopMovies[1].find('a').string)
print(len(TopMovies))