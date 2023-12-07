# -!- coding: utf-8 -!-


import requests
from bs4 import BeautifulSoup
import csv


from django.forms import forms

URL = 'https://en.wikipedia.org/wiki/Programming_languages_used_in_most_popular_websites'
HEADERS = {'user-agent' : 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                          '(KHTML, like Gecko) Chrome/93.0.4577.82 YaBrowser/21.9.0.1044 Yowser/2.5 Safari/537.36',
           'accept': '*/*'}
HOST = 'https://en.wikipedia.org/wiki/Programming_languages_used_in_most_popular_websites'
FILE = 'forms.csv'

def get_html(url, params = None) :
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_content(html) :
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all("tbody")
    items = items[0].find_all("tr")

    digits = []
    letters = []
    string = ""
    flag = True
    i = 0
    j = 0


    items.pop(0)
    people = []
    for item in items :


        popularity = item.find_all('td')
        if popularity[1]:
            for char in popularity[1].get_text(strip=True):
                if char.isalpha() or char == "[":
                    letters.append(char)
                    flag = False
                elif char.isdigit() and flag:
                    digits.append(char)
                    string += digits[j]
                    j += 1
            j = 0
            popularity = int(string)
            string = ""
            digits = []
            flag = True


        else:
            popularity = '-'

        front_end = item.find_all('td')
        if front_end[2]:
            front_end = front_end[2].get_text(strip=True)
        else:
            front_end = '-'

        back_end = item.find_all('td')
        if back_end[3]:
            back_end = back_end[3].get_text(strip=True)
        else:
            back_end = '-'

        database = item.find_all('td')
        if database[4]:
            database = database[4].get_text(strip=True)
        else:
            database = '-'

        notes = item.find_all('td')
        if notes[5]:
            notes = notes[5].get_text().replace('\n', '')
        else:
            notes = '-'



        people.append({
            'Websites' : item.find('a').get_text(strip=True),
            'Popularity': popularity,

            'Front-end': front_end,
            'Back-end': back_end,
            'Database': database,
            'Notes': notes

        })
        print(people[i])
        i += 1
    return people


def save_file(items, path) :
    with open(path, 'w', newline='', encoding="utf-8") as file:
        writer = csv.writer(file, delimiter = ';')
        writer.writerow(['Websites', 'Popularity', 'Front-end', 'Back-end', 'Database', 'Notes'])
        for item in items:
            writer.writerow(
                [item['Websites'], item['Popularity'], item['Front-end'], item['Back-end'], item['Database'], item['Notes']])

p = []

def parse() :
    global p

    html = get_html(URL)
    if html.status_code == 200:
        people = []

        people.extend(get_content(html.text))
        p = people
        save_file(people, FILE)

        check_popularity(people)
    else:
        print ('Error')

def check_popularity(items):
    popularity = 2800000000

    if items[0]['Popularity'] != popularity:
        raise forms.ValidationError("fgsd")
    return popularity

parse()
