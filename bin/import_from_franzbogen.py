import urllib.request
import urllib
import re
from bs4 import BeautifulSoup
from pprint import pprint
import csv

base_url = 'https://www.franzbogen.de/'
dir_url = 'en/assortment/'
csv_file = '../assets/Targets.csv'
target_dir = '../targets/Franzbogen'

pages = ['group+1+%28ifaa%29', 'group+2+%28ifaa%29', 'group+3+%28ifaa%29', 'group+4+%28ifaa%29',
         '3d-phantasy']


with open(csv_file, 'a', newline='') as csvfile:
    for page in pages:
        website = urllib.request.urlopen("{}{}{}".format(base_url, dir_url, page))
        html = website.read()
        soup = BeautifulSoup(html, 'html.parser')

        products = soup.find('ul', attrs={ 'id':'products'})

        items = products.find_all('li')

        for item in items:
            image = item.find('div', attrs={'class': 'image'}).find('a', attrs={'class':'lightbox'}, href=True)['href']
            name = item.find('div', attrs={'class': 'info'}).h2.text
            img_name = name.strip().replace(' ', '-')

            print("{} ==> {}".format(image, img_name))

            urllib.request.urlretrieve("{}{}".format(base_url,image), "{}/{}.png".format(target_dir,img_name))

            this_writer = csv.writer(csvfile,delimiter=',')
            this_writer.writerow(['Franzbogen','',name.strip(),"{}.png".format(img_name)])