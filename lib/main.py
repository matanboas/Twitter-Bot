from curses import keyname
from re import fullmatch
import tweepy
import requests
import os
from dotenv import load_dotenv
import urllib.request
from PIL import Image, ImageFont, ImageDraw
import textwrap

load_dotenv()

API_KEY_TWITTER = os.environ.get('API_KEY_TWITTER')
API_SECRET_TWITTER = os.environ.get('API_SECRET_TWITTER')
ACCESS_TOKEN_TWITTER = os.environ.get('ACCESS_TOKEN_TWITTER')
ACCESS_SECRET_TWITTER = os.environ.get('ACCESS_SECRET_TWITTER')

API_KEY_UNSPLASH = os.environ.get('API_KEY_UNSPLASH')
API_SECRET_UNSPLASH = os.environ.get('API_SECRET_UNSPLASH')

def get_random_photo():
    keyword='nature'

    photo_data = requests.get(f'https://api.unsplash.com/photos/random?query={keyword}&orientation=landscape&client_id={API_KEY_UNSPLASH}').json()
    image_url = photo_data['urls']['regular']

    save_name = 'images/current_picture.png'
    urllib.request.urlretrieve(image_url, save_name)

def get_quote():
    url = "https://programming-quotes-api.herokuapp.com/Quotes/random"

    response = requests.get(url).json()
    quote = response['en']
    # add newline to quote every 6 words
    quote_list = quote.split(' ')
    new_quote = ''
    for i in range(len(quote_list)):
        if i % 3 == 0 and i != 0:
            new_quote += quote_list[i] + '\n'
        else:
            new_quote += quote_list[i] + ' '
    return new_quote, response['author']



def add_text_to_image(msg):
    path = 'images/current_picture.png'
    image = Image.open(path)

    width, height = image.size
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype('fonts/Akshar-Bold.ttf', size=50)
    lines = textwrap.wrap(msg, width=40)

    textW, textH = draw.textsize(lines[0], font=font)
    fullTextH = (textH+10) * len(lines)

    y_text = ((height-fullTextH)/2)
    for line in lines:
        textW, textH = draw.textsize(line, font=font)
        draw.text(((width-textW)/2, y_text), line, (255, 255, 255), font=font)
        y_text += textH

    image.save(path)

def connect_to_twitter():
    auth = tweepy.OAuthHandler(API_KEY_TWITTER, API_SECRET_TWITTER)
    auth.set_access_token(ACCESS_TOKEN_TWITTER, ACCESS_SECRET_TWITTER)
    api = tweepy.API(auth)

    try:
        api.verify_credentials()
        print('Successful Authentication')
    except:
        print('Failed authentication')
        return None

    return api

def tweet_picture(api, message):
    
    api.update_status_with_media(message, 'images/current_picture.png')

def main():
    get_random_photo()
    msg, author = get_quote()
    add_text_to_image(msg)
    api = connect_to_twitter()
    tweet_picture(api, author)

if __name__ == '__main__':
    main()