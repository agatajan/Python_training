import tweepy
import DAY_12.exercises.tweeter.keys as keys

auth = tweepy.OAuthHandler(keys.consumer_key, keys.consumer_secret)
auth.set_access_token(keys.access_token, keys.access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

tweets = api.user_timeline(screen_name="Tesla", count=5)

for tweet in tweets:
    print(f"{15 * '='} {tweet.created_at} {15 * '='}")
    print(tweet.text)
    print(f"{15 * '='} Re-tweeted: {tweet.retweet_count} {15 * '='}", end="\n\n")