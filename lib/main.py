from curses import keyname
from re import fullmatch
import tweepy
import requests
import os
from dotenv import load_dotenv
import urllib.request
from PIL import Image, ImageFont, ImageDraw
import textwrap

load_dotenv() #load API keys

# set API keys from .env file
API_KEY_TWITTER = os.environ.get('API_KEY_TWITTER')
API_SECRET_TWITTER = os.environ.get('API_SECRET_TWITTER')
ACCESS_TOKEN_TWITTER = os.environ.get('ACCESS_TOKEN_TWITTER')
ACCESS_SECRET_TWITTER = os.environ.get('ACCESS_SECRET_TWITTER')

API_KEY_UNSPLASH = os.environ.get('API_KEY_UNSPLASH')
API_SECRET_UNSPLASH = os.environ.get('API_SECRET_UNSPLASH')

def get_random_photo(path='images/current_picture.png'):
    """get random photo from unsplash"""
    keyword='nature'

    photo_data = requests.get(f'https://api.unsplash.com/photos/random?query={keyword}&client_id={API_KEY_UNSPLASH}').json()
    image_url = photo_data['urls']['full']

    urllib.request.urlretrieve(image_url, path)

def get_quote():
    """get quote from api

    Returns:
        tuple: (quote, author)
    """    """"""
    url = "https://programming-quotes-api.herokuapp.com/Quotes/random"

    response = requests.get(url).json()
    quote = response['en']

    return quote, response['author']



def add_text_to_image(msg, path='images/current_picture.png'):
    """adds text to image

    Args:
        msg (str): message to add to image
        path (str, optional): the path to the image. Defaults to 'images/current_picture.png'.
    """
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

def tweet_picture(api, message, path='images/current_picture.png'):
    
    api.update_status_with_media(message, path)

def main():
    get_random_photo()
    #msg, author = get_quote()
    #add_text_to_image(msg)
    #api = connect_to_twitter()
    #tweet_picture(api, author)

    # app color pallete = https://colorhunt.co/palette/191a191e51284e9f3dd8e9a8

if __name__ == '__main__':
    main()