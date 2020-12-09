from get_IMDB_Top import getTopList
import random

TopMovies = getTopList()

if __name__ == "__main__":
    movieNumToWatch = random.randint(0, len(TopMovies)-1)
    printString = "Your randomly picked movie for today is {}. It is {} in IMDB TOP 250. Enjoy!".format(TopMovies[movieNumToWatch].find('a').string, (movieNumToWatch+1))
    print(printString)