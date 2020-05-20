import tweepy
import time


consumer_key = 'f5JCedV4Vly7LkOR48AAK2MRr'
consumer_secret = 'xs8vl5vySe4LopxOQEJPb5NSdGjuALhiuIRIhjr44K1ElQr6yT'
access_token = '1263161515106078720-7f6orC2QZKIw8mvo56CCOqCTpjYk4w'
access_token_secret = 'adHMf7wvJk4bTJybL0LmLfgSNZy5P1wz5auXAIfEWIBNm'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
user = api.me()


def limit_handler(cursor):
    try:
        while True:
            yield cursor.next
    except tweepy.RateLimitError:
        time.sleep(1000)


# Generous Bot

for user in limit_handler(tweepy.Cursor(api.friends).items()):
    print(user.id)
    # if user.screen_name == 'BillGates':

        # user.follow()

