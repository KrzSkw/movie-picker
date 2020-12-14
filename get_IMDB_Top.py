from bs4 import BeautifulSoup
from urllib.request import urlopen

top_url = 'https://www.imdb.com/chart/top/?sort=rk,asc&mode=simple&page=1'
page = urlopen(top_url).read()
soup = BeautifulSoup(page, 'html.parser')

def getTopList():
    movieNames = soup.find_all('td', attrs={'class': 'titleColumn'})
    return movieNames

#returns a list of movies from IMDB TOP250 with rating equal or higher than passed argument "rating"
def getTopOver(rating):
    top_movies = getTopList()
    top_movies_over = []
    top_rating = soup.find_all('td', attrs={'class': 'ratingColumn imdbRating'})
    for num, movie in enumerate(top_rating, start=0):
        if (float(movie.find('strong').string) >= rating):
            top_movies_over.append(top_movies[num].find('a').string)
    return top_movies_over


if __name__ == "__main__":
    TopMovies = getTopList()
    for movie in TopMovies:
        print(movie.find('a').string)
    topOver = getTopOver(8.8)
    print(topOver)