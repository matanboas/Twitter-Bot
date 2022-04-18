from curses import keyname
import tweepy
import requests
import os
from dotenv import load_dotenv
import urllib.request
from PIL import Image, ImageFont, ImageDraw

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

def add_text_to_image():
    image = Image.open('images/current_picture.png')
    width, height = image.size
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype('fonts/Akshar-Bold.ttf', size=50)
    msg = 'Hello World!'

    textW, textH = draw.textsize(msg, font=font)

    draw.text(((width-textW)/2,(height-textH)/2), msg, (255, 255, 255), font=font)
    image.save('images/current_picture.png')

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

def tweet_picture(api):
    
    api.update_status_with_media('', 'images/current_picture.png')

def main():
    get_random_photo()
    add_text_to_image()
    api = connect_to_twitter()
    tweet_picture(api)

if __name__ == '__main__':
    main()