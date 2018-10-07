import tweepy
import readlines

def sendTweet(message):
    #getting from text file
    result = readlines.getAllLinesIn('twitterid.txt')
    #twitter application credentials
    consumer_key=result[0]
    consumer_secret=result[1]
    #twitter user credentials
    access_token=result[2]
    access_token_secret=result[3]
    #setting up API
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    tweepyapi = tweepy.API(auth)
    #tweeting
    try:
        if tweepyapi.update_status(message):
            print("Sent tweet: " + message)
    except tweepy.error.TweepError as e:
        print("Error sending tweet: " + e)

if __name__ == "__main__":
    sendTweet("Testing a tweet!")