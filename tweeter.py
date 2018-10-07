import tweepy
import readlines
#getting from text file
result = readlines.getAllLinesIn('twitterid.txt')
#twitter application credentials
consumer_key=result[0]
consumer_secret=result[1]

#twitter user credentials
access_token=result[2]
access_token_secret=result[3]

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

tweepyapi = tweepy.API(auth)

tweepyapi.update_status('Hello World!! Again')