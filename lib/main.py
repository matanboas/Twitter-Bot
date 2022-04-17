import os
from dotenv import load_dotenv

#os.environ['TWITTER_CONSUMER_KEY'] = 'RSp9hVwFwihFyPnkrCDH99jAT'
#os.environ['TWITTER_CONSUMER_SECRET'] = 'YZL5hoZu8w570vnpI0N2Fbcpdhtdd1pDYxkixot90Q1M4qGODR'

load_dotenv()

USER = os.environ.get('TWITTER_CONSUMER_KEY')
PASSWORD = os.environ.get('TWITTER_CONSUMER_SECRET')

print(USER)
print(PASSWORD)