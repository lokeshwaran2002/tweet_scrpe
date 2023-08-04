import tweepy
import pandas as pd

# Set your API keys and access tokens
consumer_key = 'YOUR_CONSUMER_KEY'
consumer_secret = 'YOUR_CONSUMER_SECRET'
access_token = 'YOUR_ACCESS_TOKEN'
access_secret = 'YOUR_ACCESS_SECRET'

# Authenticate with the Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

# List of hashtags to scrape
hashtags = ["your", "list", "of", "hashtags"]

# Data storage
data = []

# Scrape and extract data
for hashtag in hashtags:
    tweets = tweepy.Cursor(api.search, q=hashtag, lang='en').items()
    for tweet in tweets:
        user = tweet.user.screen_name
        location = tweet.user.location
        created_at = tweet.created_at
        data.append({'User': user, 'Location': location, 'Date': created_at})

# Create a DataFrame for analysis
df = pd.DataFrame(data)

# Group by user and month, calculate tweet counts
df['Month'] = df['Date'].dt.to_period('M')
result = df.groupby(['User', 'Month']).size().reset_index(name='Tweet_Count')

# Export to CSV
result.to_csv('tweet_counts_by_user.csv', index=False)
