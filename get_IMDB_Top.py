from bs4 import BeautifulSoup
from urllib.request import urlopen

top_url = 'https://www.imdb.com/chart/top/?sort=rk,asc&mode=simple&page=1'
page = urlopen(top_url).read()
soup = BeautifulSoup(page, 'html.parser')

def getTopList():
    movieNames = soup.find_all('td', attrs={'class': 'titleColumn'})
    return movieNames


def getTopOver(rating):
    top_movies = getTopList()
    top_rating = soup.find_all('td', attrs={'class': 'ratingColumn imdbRating'})
    for num, movie in enumerate(top_rating, start=1):
        if (float(movie.find('strong').string) >= rating):
            print(movie.find('strong').string)
            print(num)




if __name__ == "__main__":
    #TopMovies = getTopList()
    #for movie in TopMovies:
    #    print(movie.find('a').string)
    getTopOver(9)