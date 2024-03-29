import urllib2
from bs4 import BeautifulSoup

mp3_url = "http://www.mp3skull.com/mp3/"

## Returns the download link from mp3skull given the information
## about the song.
def scrap(dict):
	url =  dict["artist"] + "_" + dict["name"]
	final_meta_data = {}
	temp_url = mp3_url + url + ".html"
	soup = BeautifulSoup(urllib2.urlopen(temp_url).read())
	songs = soup.findAll('div', {'id':'song_html'})
	counter = 1
	for song in songs:
		temp_lst = extract_meta(song)
		link = song.findAll('a', {'style' : 'color:green;'})
		download_link = link[0].get('href')
		download_link.replace("u'^", '')
		temp_lst.append(download_link)
		final_meta_data[str(counter)] = temp_lst
		counter += 1
	return final_meta_data

## Returns a list of meta data from mp3skull
def extract_meta(tag):
	final_meta_list = []
	meta = str(tag.findAll('div', {'class':'left'})).split('<br/>')
	bitrate = meta[0].split('\t')
	time = meta[1]
	filesize = meta[2].split('\t')[0]
	final_meta_list.append(bitrate[len(bitrate) - 1])
	final_meta_list.append(time)
	final_meta_list.append(filesize)
	return final_meta_list