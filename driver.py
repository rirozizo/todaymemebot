import tweepy
import random

from datetime import datetime

today = datetime.today().strftime('%Y-%m-%d')
day = int(datetime.today().strftime('%d'))
month = int(datetime.today().strftime('%m'))
year = int(datetime.today().strftime('%Y'))



auth = tweepy.OAuthHandler("API Key", "API Secret")

auth.set_access_token("Access Token", "Access Token Secret")

api = tweepy.API(auth)


def zeller(date, month, year):   # Day, Month, Year in full
    if (month < 3):
        # January and February are months 13 and 14 of the previous year
        month += 12
        year -= 1;
        
    # separate out the century and year parts
    j = int(year / 100)
    k = int(year % 100)
    
    # calculate the day of the week
    dow = int((date + ((13 * (month + 1)) / 5) + k + int(k / 4) + int(j / 4) + (5 * j)) % 7)

    if dow == 1:
        day = "Sunday"
    elif dow == 2:
        day = "Monday"
    elif dow == 3:
        day = "Tuesday"
    elif dow == 4:
        day = "Wednesday"
    elif dow == 5:
        day = "Thursday"
    elif dow == 6:
        day = "Friday"
    else:
        day = "Saturday"

    return day

dayname = zeller(day,month,year)
print('Today is', dayname)

import requests, shutil, json
url = 'https://meme-api.herokuapp.com/gimme'
data = {"postLink":"","url":""}
response = requests.get(url, data=data)
print(response.text)
j = json.loads(response.text)
image_url = j['url']
reddit = j['postLink']
resp = requests.get(image_url, stream=True)
local_file = open('/home/pi/twitter/local_image.jpg', 'wb')
resp.raw.decode_content = True
shutil.copyfileobj(resp.raw, local_file)
del resp

#links = open('/home/pi/twitter/links.txt').read().splitlines()
#random_link =random.choice(links)
#print('A Random YouTube video of mine: https://www.youtube.com/watch?v={0}'.format(random_link))
print('Tweeting...')
api.update_with_media("/home/pi/twitter/local_image.jpg", status = 'Today is a {0}\nHere\'s A Random Meme from {1}'.format(dayname, reddit))
print('done')