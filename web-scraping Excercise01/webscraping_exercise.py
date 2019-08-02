from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import requests

# Opens the url using urlopen by using try except block and if found error throws error.
print("-"*10, "ONE", "-"*10)

try:
    page = urlopen('https://www.flipkart.com/jj')
except:
    print("Page not found")
else:
    print("no error")
finally:
    print("runs everytime")

# opens robots.txt file of www.wikipedia.org and parses it into lxml and also prints it
print("-"*10, "TWO", "-"*10)

page = urlopen('https://www.wikipedia.org//robots.txt')
data = bs(page, 'lxml')
error = data.prettify()
print(error)

# opens 'https://catalog.data.gov/dataset' and then find the number of datasets present
print("-"*10, "THREE", "-"*10)
page = urlopen('https://catalog.data.gov/dataset')
data = bs(page, 'lxml')
data_set = data.find_all('div', class_="dataset-content")
print(data_set.__len__())

# opens  "http://maps.googleapis.com/maps/api/geocode/json" and requests website to provide latitude and longitude of
# the input address
print("-"*10, "FOUR", "-"*10)

url = "http://maps.googleapis.com/maps/api/geocode/json"
address = {'address': '1600 Amphitheatre Parkway, Mountain View, CA'}
response = requests.get(url, params=address)
print(response.json())


# opens the 'https://catalog.data.gov/' and prints the headings of each dataset
print("-"*10, "FIVE", "-"*10)

page = urlopen('https://catalog.data.gov/dataset?q=&sort=metadata_created+desc&as_sfid=AAAAAAWDu21WPZd4IbrtgHY-xzaPn-N2HPPq1sh44woWrNP6z-Aw6gbF_KacznxbXKTJlU6nGN5GCa_rBGnmbqjpYw6vGjLiI2HrVerxS7agi_EUM1mMipM72Y23aV60T1mOoB0%3D&as_fid=d2c1f3204684c5fd39fd0eaf0bdd0159faec8031&ext_location=&ext_bbox=&ext_prev_extent=-142.03125%2C2.4601811810210052%2C-59.0625%2C58.63121664342478')
data_set = data.find('h3', class_="dataset-heading")
print(data_set.a.text)

# opens 'http://www.example.com/' and finds all h1 and print their content
print("-"*10, "SIX", "-"*10)

page = urlopen('http://www.example.com/')
data = bs(page, 'lxml')
data_set = data.find('h1')
print(data_set.text)


# open 'https://en.wikipedia.org/wiki/Main_Page' and prints all 'h1', 'h2', 'h3', 'h4', 'h5', 'h6' heading
print("-"*10, "SEVEN", "-"*10)

page = urlopen('https://en.wikipedia.org/wiki/Main_Page')
data = bs(page, 'lxml')
j = 0
data_set = []
list_name = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']
data_set = data.find_all((list_name))
for i in data_set:
    print(i.text)

# open 'https://en.wikipedia.org/wiki/Peter_Jeffrey_(RAAF_officer)' and prints the links of all images present in the
# webpages
print("-"*10, "EIGHT", "-"*10)

page = urlopen('https://en.wikipedia.org/wiki/Peter_Jeffrey_(RAAF_officer)')
data = bs(page, 'lxml')
data_set = data.find_all('img')
for i in data_set:
    print(i['src'])


print("-"*10, "NINE", "-"*10)

page = requests.get('https://analytics.usa.gov/data/live/browsers.json')
print(page.json()['totals']['browser'])

print("-"*10, "TEN", "-"*10)

page = urlopen('https://en.wikipedia.org/wiki/Python')
data = bs(page, 'lxml')
data_set = data.find_all('a')
for i in data_set:
    print(i.text)

print("-"*10, "END", "-"*10)
