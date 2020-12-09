from bs4 import BeautifulSoup
from urllib.request import urlopen

def getTopList():
    top_url = 'https://www.imdb.com/chart/top/?sort=rk,asc&mode=simple&page=1'
    page = urlopen(top_url).read()
    soup = BeautifulSoup(page, 'html.parser')
    movieNames = soup.find_all('td', attrs={'class': 'titleColumn'})
    return movieNames




if __name__ == "__main__":
    TopMovies = getTopList()
    for movie in TopMovies:
        print(movie.find('a').string)