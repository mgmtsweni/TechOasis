import tweepy
import pandas as pd
from textblob import TextBlob

'''before use, install these 3 modu tweeplesy, pandas, textblob'''

# Step 1: Authenticate your app with Twitter API credentials
API_KEY = 'your-api-key'
API_SECRET_KEY = 'your-api-secret-key'
ACCESS_TOKEN = 'your-access-token'
ACCESS_TOKEN_SECRET = 'your-access-token-secret'

# Step 2: Set up authentication
auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# Step 3: Create an API object to interact with Twitter
api = tweepy.API(auth, wait_on_rate_limit=True)

# Step 4: Define a function to analyze sentiment using TextBlob
def analyze_sentiment(tweet_text):
    analysis = TextBlob(tweet_text)
    if analysis.sentiment.polarity > 0:
        return 'Positive'
    elif analysis.sentiment.polarity == 0:
        return 'Neutral'
    else:
        return 'Negative'

# Step 5: Define a function to search tweets and save to a CSV file
def search_tweets(keyword, count=10, output_file='tweets_data.csv'):
    tweets_data = []
    
    # Search for tweets containing the keyword
    tweets = api.search_tweets(q=keyword, count=count, tweet_mode='extended', lang='en')
    
    for tweet in tweets:
        username = tweet.user.screen_name
        text = tweet.full_text
        location = tweet.user.location
        created_at = tweet.created_at
        geo = tweet.geo
        sentiment = analyze_sentiment(text)  # Analyze sentiment
        
        # Append data to the list
        tweets_data.append({
            'Username': username,
            'Tweet': text,
            'Location': location,
            'Time': created_at,
            'Geo': geo,
            'Sentiment': sentiment
        })
    
    # Convert the list of dictionaries to a pandas DataFrame
    df = pd.DataFrame(tweets_data)
    
    # Save the DataFrame to a CSV file
    df.to_csv(output_file, index=False)
    print(f"Data saved to {output_file}")

# Step 6: Search for tweets with a specific keyword and save to a file
if __name__ == "__main__":
    keyword = input("Enter a keyword to search for: ")
    tweet_count = int(input("How many tweets would you like to retrieve? "))
    output_file = input("Enter the filename to save the data (e.g., tweets.csv): ")
    
    search_tweets(keyword, count=tweet_count, output_file=output_file)
