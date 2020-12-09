from bs4 import BeautifulSoup
from urllib.request import urlopen

top_url = 'https://www.imdb.com/chart/top/?sort=rk,asc&mode=simple&page=1'

page = urlopen(top_url).read()
soup = BeautifulSoup(page, 'html.parser')

movieNames = soup.find_all('td', attrs={'class': 'titleColumn'})




if __name__ == "__main__":
    for movie in movieNames:
        print(movie.find('a').string)