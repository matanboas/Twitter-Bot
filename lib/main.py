import os
from dotenv import load_dotenv

load_dotenv()

USER = os.environ.get('TWITTER_CONSUMER_KEY')
PASSWORD = os.environ.get('TWITTER_CONSUMER_SECRET')

print(USER)
print(PASSWORD)