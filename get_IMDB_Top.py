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

#this function returns only movies from TOP250 that were poduced later than minYear and before maxYear
def getTopByDate(minYear, maxYear):
    top_movies = getTopList()
    top_year = soup.find_all('', attrs={'class': 'secondaryInfo'})
    top_movies_year = [],[]
    for num, year in enumerate(top_year, start=0):
        if (int(year.text[1:-1]) >= minYear and int(year.text[1:-1]) <= maxYear):
            top_movies_year[0].append(top_movies[num].find('a').string)
            top_movies_year[1].append(year.text[1:-1])
    return top_movies_year
    


if __name__ == "__main__":
    ### Just some testing calls and prints ###
    # TopMovies = getTopList()
    # for movie in TopMovies:
    #     print(movie.find('a').string)
    #topOver = getTopOver(8.8)
    #print(topOver)
    #top_years = getTopByDate(1995,1998)
    #print(top_years)

