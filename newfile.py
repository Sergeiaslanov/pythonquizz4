import requests,csv,random
from bs4 import BeautifulSoup as bs
from time import sleep

def main():
	f = open('moviesge.csv','w',encoding='utf-8_sig',newline='\n')
	f_obj = csv.writer(f)
	f_obj.writerow(['movie name','release year','imdb'])
	
	movieTitles, movieYears, movieImdb = [],[],[]
	page  = 1
	while True:
		url = 'https://movie.ge/filter-movies?type=movie&page={}'.format(page)
		r = requests.get(url)
		soup = bs(r.text,'html.parser')

		''' for movie titles '''
		movie_titles_div = soup.find_all('div',class_='popular-card__title')
		for div in movie_titles_div:
			movieTitles.append(div.a.p.text)

		''' for years '''
		sub_soup = soup.find_all('div',class_='popular-card__img')
		for x in sub_soup:
			movieYears.append(x.find('div',class_='year').text)


		''' for imdb '''
		movie_imdb_div = soup.find_all('div',class_='imdb')
		for div in movie_imdb_div:
			movieImdb.append(div.span.text)

		if page == 5:
			print('all information was saved to the "moviesge.csv" file.')
			for x in range(len(movieTitles)):
				f_obj.writerow([movieTitles[x],movieYears[x],movieImdb[x]])
			break
		else:
			page += 1
			print('sending request to the {} page of website...'.format(page))
			sleep(random.randint(8,15))
main()