import pandas as pd
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs

word = input("Enter the word to be searched")
page = urlopen('https://arxiv.org/search/?query='+word+'&searchtype=all&abstracts=show&order=-announced_date_first&size=50')
soup = bs(page, 'lxml')
h = soup.find_all('li', class_="arxiv-result")

#finds all the headlines and removes unwanted characters form it and also returns the list of all Headings
def Head(i, att, cl):
    global h
    head = h[i].find(att, class_= cl).text.strip()
    return head


def Auth(i, att, cl):
    global h
    s = ""
    a = h[i].find(att, class_= cl).text
    for j in a.split(","):
        s = s + str(j).strip().replace('Authors:\n', '') + " "
    return s


def Date(i, att, cl):
    global h
    a = h[i].find(att, class_= cl).text.split(";")[0].replace("Submitted", "")
    return a


def Summary(i, att, cl):
    global h
    a = h[i].find(att, class_= cl).text.strip()
    return a


Header1 = list()
Author1 = list()
Submitted1 = list()
Description1 = list()

for i in range(h.__len__()):
    Header1.append(Head(i, 'p', 'title is-5 mathjax'))
    Author1.append(Auth(i, 'p', "authors"))
    Submitted1.append(Date(i, 'p', "is-size-7"))
    Description1.append(Summary(i, 'span', "abstract-short has-text-grey-dark mathjax"))

isbn = []
doi = []
source = []
for i in range(Header1.__len__()):
    isbn.append("Not Available")
    doi.append("Not Available")
    source.append("arxiv.org")
df1 = pd.DataFrame({'Heading': Header1, "Author": Author1, "Description": Description1, "Submittion Date": Submitted1,
                   "ISBN No.": isbn, "DOI No.": doi, "Source": source})


page = urlopen('https://eric.ed.gov/?q='+word)
soup = bs(page, 'lxml')
h = soup.find_all('div', class_="r_i")


def Auth2(i, att, cl):
    global h
    al = ""
    a = h[i].find(att, class_= cl).text.split("–")[0].split(";")
    for j in a:
        f = j.split(",")[1]
        l = j.split(",")[0]
        final = str(f) + " " + str(l)
        al = al + str(final) + " , "
    return al


def Summary2(i, att, cl):
    global h
    a = h[i].find(att, class_= cl).text.strip()
    return a


Header2 = list()
Author2 = list()
Description2 = list()
for i in range(h.__len__()):
    Header2.append(Head(i, 'div', 'r_t'))
    Author2.append(Auth2(i, "div", "r_a"))
    Description2.append(Summary2(i, "div", "r_d"))
doi = list()
isbn = list()
submitted2 = list()
source = list()
for i in range(Header2.__len__()):
    doi.append("Not Available")
    isbn.append("Not Available")
    submitted2.append("Not Available")
    source.append('eric.ed.gov/')
df2 = pd.DataFrame({'Heading': Header2, "Author": Author2, "Description": Description2, "Submittion Date": submitted2,
                    "ISBN No.": isbn, "DOI No.": doi, "Source": source})


page = urlopen('https://www.researchgate.net/search/publications?q='+'word')
soup = bs(page, 'lxml')
h = soup.find_all('div', class_="nova-v-publication-item__stack nova-v-publication-item__stack--gutter-m")


def Auth3(i, att, cl):
    global h
    al = ""
    a = h[i].find_all(att, class_= cl)
    for j in a:
        al = al + str(j.text) + ", "
    return al


def Last(i, att, cl):
    al = []
    a = h[i].find_all(att, class_=cl)
    for j in a:
        al.append(j.text)
    if al.__len__() < 3:
        for j in range(3-al.__len__()):
            al.append(0)
    return al


Header3 = list()
Author3 = list()
Date3 = list()
ISBN = list()
DOI = list()
for i in range(h.__len__()):
    Header3.append(Head(i, 'div', 'nova-e-text nova-e-text--size-l nova-e-text--family-sans-serif nova-e-text--spacing-none nova-e-text--color-inherit nova-v-publication-item__title'))
    Author3.append(Auth3(i, 'span', 'nova-v-person-inline-item__fullname'))
    item = Last(i, 'li', 'nova-e-list__item nova-v-publication-item__meta-data-item')
    if item[0]:
        Date3.append(item[0])
    else:
        Date3.append("Not Available")
    if item[1]:
        DOI.append(item[1])
    else:
        DOI.append("Not Available")
    if item[2]:
        ISBN.append(item[2])
    else:
        ISBN.append("Not Available")
source = list()
description = list()
for i in range(Header3.__len__()):
    source.append('www.researchgate.net')
    description.append('Not Available')
df3 = pd.DataFrame({'Heading': Header3, "Author": Author3, "Description": description, "Submittion Date": Date3,
                    "ISBN No.": ISBN, "DOI No.": DOI, "Source": source})
df4 = pd.concat([df3, df2], ignore_index=1)
final = pd.concat([df4, df1], ignore_index=1)
final.to_csv('final.csv')